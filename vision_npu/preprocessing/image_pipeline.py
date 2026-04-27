from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ImagePreprocessConfig:
    size: tuple[int, int]
    mean: tuple[float, float, float]
    std: tuple[float, float, float]
    color_format: str = "rgb"


DEFAULT_IMAGE_PREPROCESS = ImagePreprocessConfig(
    size=(224, 224),
    mean=(0.485, 0.456, 0.406),
    std=(0.229, 0.224, 0.225),
)
