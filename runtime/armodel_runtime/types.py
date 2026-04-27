from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RuntimeInput:
    image: Path | bytes
    robot_state: tuple[float, ...]
    instruction: str | None = None


@dataclass(frozen=True)
class RuntimeOutput:
    action: tuple[float, ...]
    metadata: dict[str, Any]
