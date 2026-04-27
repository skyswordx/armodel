from __future__ import annotations

from .loader import ModelArtifact
from .types import RuntimeInput, RuntimeOutput


class InferencePipeline:
    def __init__(self, artifact: ModelArtifact) -> None:
        self.artifact = artifact

    def infer(self, runtime_input: RuntimeInput) -> RuntimeOutput:
        raise NotImplementedError(
            "Backend-specific inference is implemented after an exported artifact is available."
        )
