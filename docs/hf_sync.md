# Hugging Face Sync

Create a manifest under `smoVLA/hf/manifests/`.

Required fields:

- `repo_id`: Hugging Face repository ID.
- `revision`: Commit SHA, tag, or branch name.
- `local_dir`: Local snapshot path.

Use a commit SHA when the model must be reproducible.

Run:

```powershell
python scripts/hf_download.py smoVLA/hf/manifests/<model>.yaml --dry-run
python scripts/hf_download.py smoVLA/hf/manifests/<model>.yaml
```

Commit the manifest and update `smoVLA/hf/manifests/smovla_versions.lock` after verification.
