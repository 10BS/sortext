from typing import Literal
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Entry:
    abs_path: Path
    name: str
    ext: str
    type: Literal["file", "dir"]
