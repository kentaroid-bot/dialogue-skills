#!/usr/bin/env python3
"""Check distribution metadata; build versioned archives from committed Git files."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NAMES = ("dialogue-essay", "dialogue-prompt", "dialogue-checker", "dialogue-publisher")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def validate(read):
    portable = json.loads(read("plugin.json"))
    overlay = json.loads(read(".codex-plugin/plugin.json"))
    for key in ("name", "version", "description", "author", "homepage", "repository"):
        if portable.get(key) != overlay.get(key):
            raise ValueError(f"Manifest mismatch: {key}")
    if portable["name"] != "dialogue-skills":
        raise ValueError("Unexpected plugin name")
    version = portable["version"]
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:[-+][0-9A-Za-z.-]+)?", version):
        raise ValueError("Invalid version")
    catalog = json.loads(read(".agents/plugins/marketplace.json"))
    entry, = catalog["plugins"]
    if catalog["name"] != "dialogue-skills" or entry["name"] != portable["name"]:
        raise ValueError("Catalog identity mismatch")
    if entry["source"] != {
        "source": "url",
        "url": portable["repository"] + ".git",
        "ref": "main",
    }:
        raise ValueError("Catalog must point to the published GitHub plugin")
    if entry["policy"] != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
        raise ValueError("Unexpected installation policy")
    if entry["category"] != "Productivity":
        raise ValueError("Unexpected category")
    for name in NAMES:
        body = read(f"skills/{name}/SKILL.md").decode("utf-8")
        if not body.startswith("---\n") or f"\nname: {name}\n" not in body:
            raise ValueError(f"Missing skill identity: {name}")
    return version


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="Build the committed HEAD release")
    args = parser.parse_args()
    if not args.build:
        version = validate(lambda name: (ROOT / name).read_bytes())
        print(f"Distribution metadata and four skill identities valid: {version}")
        return

    commit = git("rev-parse", "HEAD").decode().strip()
    read = lambda name: git("show", f"{commit}:{name}")
    version = validate(read)
    paths = git("ls-tree", "-rz", "--name-only", commit).decode().split("\0")
    skill_files = [p for p in paths if any(p.startswith(f"skills/{n}/") for n in NAMES)]
    files = ["plugin.json", ".codex-plugin/plugin.json", "README.md", "LICENSE-dialogue-essay"] + skill_files
    files += [p for p in paths if p.startswith("docs/")]
    output = ROOT / ".local" / "releases" / version
    output.mkdir(parents=True, exist_ok=True)
    records = {}

    def archive(name, members):
        path = output / name
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as target:
            for original, packaged in members:
                target.writestr(packaged, read(original))
        records[name] = hashlib.sha256(path.read_bytes()).hexdigest()

    archive(f"dialogue-skills-{version}.zip", [(p, f"dialogue-skills/{p}") for p in files])
    for name in NAMES:
        archive(f"{name}-{version}.zip", [
            (p, p.removeprefix("skills/")) for p in skill_files if p.startswith(f"skills/{name}/")
        ])
    result = {
        "version": version,
        "commit": commit,
        "skill_sha256": {name: hashlib.sha256(read(f"skills/{name}/SKILL.md")).hexdigest() for name in NAMES},
        "archive_sha256": records,
    }
    (output / "release.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
