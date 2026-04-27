from pathlib import Path

from runtime.armodel_runtime import load_export_manifest


def test_load_export_manifest_reads_artifact_path() -> None:
    artifact = load_export_manifest(Path("smoVLA/export/onnx/export_manifest.example.yaml"))

    assert artifact.name == "smovla-example-onnx"
    assert artifact.format == "onnx"
    assert artifact.path == Path("smoVLA/export/onnx/smovla-example.onnx")
