from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml
from huggingface_hub import snapshot_download


REQUIRED_FIELDS = ("repo_id", "revision", "local_dir")


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle) or {}

    missing = [field for field in REQUIRED_FIELDS if not manifest.get(field)]
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"{path} is missing required field(s): {joined}")

    return manifest


def download_from_manifest(path: Path, dry_run: bool = False) -> Path:
    manifest = load_manifest(path)
    local_dir = Path(manifest["local_dir"])

    if dry_run:
        print(f"repo_id={manifest['repo_id']}")
        print(f"revision={manifest['revision']}")
        print(f"local_dir={local_dir}")
        return local_dir

    snapshot_download(
        repo_id=manifest["repo_id"],
        revision=manifest["revision"],
        local_dir=local_dir,
        allow_patterns=manifest.get("allow_patterns"),
        ignore_patterns=manifest.get("ignore_patterns"),
        local_dir_use_symlinks=False,
    )
    return local_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a Hugging Face model snapshot.")
    parser.add_argument("manifest", type=Path, help="Path to a Hugging Face source manifest.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print manifest values.")
    args = parser.parse_args()

    downloaded_path = download_from_manifest(args.manifest, dry_run=args.dry_run)
    print(downloaded_path)


if __name__ == "__main__":
    main()
