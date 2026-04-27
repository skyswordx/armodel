# armodel

`armodel` is the model-side workspace for the Roboclaw arm stack.

This repository keeps code, configuration, manifests, and small examples in Git.
Large model weights, datasets, checkpoints, exported inference engines, and local caches stay outside Git.

## Scope

- Pull base `smoVLA` models from Hugging Face by manifest.
- Manage `smoVLA` post-training recipes, adapters, and checkpoints.
- Export trained models to deployment formats such as ONNX, TorchScript, and NPU engines.
- Maintain vision-recognition preprocessing and NPU backend integration.
- Provide runtime loading and inference entry points for the arm stack.

## Layout

```text
configs/
  smovla/            Training, export, and inference configuration.
  vision_npu/        Vision preprocessing, quantization, and backend configuration.
scripts/             CLI utilities for download, training, export, conversion, and inference.
smoVLA/
  hf/                Hugging Face manifests, lock files, and local snapshot mount points.
  post_training/     Dataset notes, recipes, adapters, and checkpoint mount points.
  export/            Export manifests and local exported model mount points.
vision_npu/          Vision preprocessing, calibration, and NPU backend adapters.
runtime/             Runtime loader, pipeline, types, and examples.
docs/                Asset policy and workflow notes.
tests/               Lightweight tests for config and runtime code.
```

## Hugging Face model flow

1. Copy `smoVLA/hf/manifests/smovla_template.yaml` to a model-specific manifest.
2. Fill in the real Hugging Face `repo_id`, immutable `revision`, file allow list, and local cache path.
3. Run:

```powershell
python scripts/hf_download.py smoVLA/hf/manifests/<model>.yaml
```

The downloaded snapshot is stored under `smoVLA/hf/snapshots/` and is ignored by Git.
Commit only the manifest and lock metadata needed to reproduce the download.

## Asset policy

Git tracks:

- Source code and tests.
- YAML configuration.
- Hugging Face source manifests.
- Export manifests.
- Small format examples.
- `.gitkeep` files for empty artifact directories.

Git does not track:

- Datasets.
- Hugging Face model snapshots.
- Checkpoints and adapters.
- ONNX, TorchScript, RKNN, TensorRT, and other exported engines.
- Local experiment outputs.

Use `docs/model_asset_policy.md` before adding any large file to this repository.
