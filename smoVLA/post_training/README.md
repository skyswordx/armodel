# Post-Training

This directory stores reproducible training inputs and metadata.

- `datasets/` contains dataset format notes, manifests, and tiny examples.
- `recipes/` contains training recipes such as LoRA and full fine-tuning.
- `adapters/` is a local output target and is ignored by Git.
- `checkpoints/` is a local output target and is ignored by Git.

Each real training run should produce a manifest that records the base model revision, dataset revision, recipe file, dependency versions, and output path.
