# Model Asset Policy

Git in this repository is for source code, configuration, manifests, documentation, tests, and small examples.

Do not commit large model or dataset files.
Use Hugging Face manifests for base models and local ignored directories for downloaded snapshots.
Use export manifests for generated deployment artifacts.

Tracked files should answer:

- Which source model was used.
- Which revision was used.
- Which training recipe or export config produced an artifact.
- Which local path is expected when running on a machine that has the artifact.

Ignored files include model snapshots, datasets, checkpoints, adapters, ONNX files, RKNN files, TensorRT engines, and experiment outputs.
