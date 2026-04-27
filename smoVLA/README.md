# smoVLA Workspace

This directory separates source model retrieval, post-training, and deployment exports.

- `hf/` records Hugging Face model sources and local snapshot mount points.
- `post_training/` stores dataset notes, recipes, adapters, and checkpoint mount points.
- `export/` stores export manifests and local exported model mount points.

Only metadata and small examples belong in Git.
Model snapshots, adapters, checkpoints, and exported engines are ignored.
