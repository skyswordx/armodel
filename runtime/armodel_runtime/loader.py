from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ModelArtifact:
    name: str
    format: str
    path: Path
    manifest_path: Path
    metadata: dict[str, Any]


def load_export_manifest(manifest_path: str | Path) -> ModelArtifact:
    path = Path(manifest_path)
    with path.open("r", encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle) or {}

    output = manifest.get("output") or {}
    output_path = output.get("path")
    if not output_path:
        raise ValueError(f"Export manifest {path} is missing output.path")

    return ModelArtifact(
        name=str(manifest.get("name", path.stem)),
        format=str(manifest.get("format", "")),
        path=Path(output_path),
        manifest_path=path,
        metadata=manifest,
    )
