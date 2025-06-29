import json
import os
from dataclasses import dataclass
from os import PathLike
from typing import Literal


@dataclass(frozen=True)
class Entry:
    path: str
    name: str
    ext: str
    type: Literal["file", "dir"]


def list_entries(
    path: str = ".",
    entry_type: Literal["all", "file", "dir"] = "all",
    save: bool = False
) -> list[dict[str, str | bool]]:
    entries: list = []
    for entry in os.scandir(path):
        basename, dot_ext = os.path.splitext(entry.name)
        ext: str = dot_ext[1:]
        entry = Entry(
            path = os.path.abspath(entry),
            name = basename,
            ext = ext,
            type = "file" if os.path.isfile(entry) else "dir",
        )
        if entry_type == "all":
            entries.append(entry)
        elif entry_type == "file":
            entries.append(entry) if entry.type is "file" else None
        elif entry_type == "dir":
            entries.append(entry) if entry.type is "dir" else None

    if save:
        with open(f"{path}\\entries.txt", "w", encoding="utf-8") as dump:
            print(entry.__repr__())

    return entries


def filter_by_ext(path: str, *pool_ext):
    filtered = []
    for entry in list_entries(path, "file"):
        if entry["ext"] in pool_ext:
            filtered.append(entry)

    return filtered


list_entries(save=True)
