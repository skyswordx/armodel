# armodel

`armodel` is a model-side workspace for the Roboclaw arm stack.

The repository is intended to hold future work for:

- vision recognition with NPU acceleration;
- smoVLA post-training assets and experiments;
- smoVLA inference runtime integration.

## Layout

- `vision_npu/`: vision recognition and NPU acceleration work.
- `smoVLA/`: smoVLA post-training experiments, adapters, and model assets.
- `runtime/`: inference entry points, deployment notes, and runtime adapters.

Large model files, datasets, checkpoints, and exported runtime binaries should stay out of Git unless a storage policy is added.
