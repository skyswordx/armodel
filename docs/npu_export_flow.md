# NPU Export Flow

Recommended flow:

1. Download the base model from a Hugging Face manifest.
2. Run post-training and store adapters or checkpoints in ignored output directories.
3. Export to ONNX or TorchScript.
4. Convert the exported artifact to a target NPU backend.
5. Commit only the export manifest and backend configuration.

The runtime should load model metadata from the export manifest.
It should not infer paths from training output directories.
