import os
from dataclasses import dataclass
from enum import unique
from pathlib import Path
from typing import Literal


@dataclass(frozen=True)
class Entry:
    path: Path
    name: str
    ext: str | list[str]
    type: Literal["file", "dir"]


@dataclass(frozen=True)
class Exts:
    common_exts: list[str]
    unique_exts: list[str]


with open("exts.txt", "r", encoding="utf-8") as file:
    exts_list = file.read().splitlines()


def list_exts(path, exts_list) -> Exts:
    common_exts = []
    unique_exts = []
    exts = Exts(common_exts, unique_exts)
    for entry in os.scandir(path):
        ext = "".join(Path(entry).suffixes)
        if ext in exts_list:
            common_exts.append(ext)
        elif not ext in exts_list and ext:
            unique_exts.append(ext)
    return exts


def list_entries(
    path: str = "test",
    entry_type: Literal["all", "file", "dir"] = "all",
) -> list[Entry]:
    entries: list = []
    for entry in os.scandir(path):
        ext = "".join(Path(entry).suffixes)
        basename = Path(entry).name
        entry = Entry(
            path = Path(path, entry).absolute(),
            name = basename,
            ext = ext,
            type = "file" if os.path.isfile(entry) else "dir",
        )
        if entry_type == "all":
            entries.append(entry)
        elif entry_type == "file":
            entries.append(entry) if entry.type == "file" else None
        elif entry_type == "dir":
            entries.append(entry) if entry.type == "dir" else None
    return entries


def filter_entries(path: str, string: str, *pool_ext):
    filtered = []
    for entry in list_entries(path, "file"):
        if pool_ext:
            if entry.ext in pool_ext:
                filtered.append(entry)
        else:
            filtered.append(entry)
    return filtered


print(list_exts(".", exts_list))
