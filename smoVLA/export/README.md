# Export

This directory stores export metadata and local output mount points.

- `onnx/` is for ONNX export manifests and local ONNX artifacts.
- `torchscript/` is for TorchScript export manifests and local artifacts.
- `npu/` is for NPU compiler output such as RKNN or TensorRT engines.

Exported model files are ignored.
Commit the manifest that records the source checkpoint, format, input shapes, precision, and converter version.
