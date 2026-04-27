from pathlib import Path

from armodel_runtime import load_export_manifest


def main() -> None:
    artifact = load_export_manifest(Path("smoVLA/export/onnx/export_manifest.example.yaml"))
    print(f"Loaded {artifact.name} ({artifact.format}) from {artifact.path}")


if __name__ == "__main__":
    main()
