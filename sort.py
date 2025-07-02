import os
from pathlib import Path
from re import Pattern
from typing import Literal

from data_classes import Entry


def list_entries(
    path: str = ".",
    entry_type: Literal["all", "file", "dir"] = "all",
) -> list[Entry]:
    entries: list[Entry] = []
    with open("exts.txt", "r", encoding="utf-8") as file:
        suffixes: tuple[str, ...] = tuple(file.read().splitlines())
    for dir_entry in os.scandir(path):
        filename = dir_entry.name
        matched_suffix = next((ext for ext in suffixes if filename.endswith(ext)), None)

        if matched_suffix:
            base_name = filename[: -len(matched_suffix)]
            ext = matched_suffix
            if base_name == "" and dir_entry.is_dir():
                base_name = ext
                ext = ""
        else:
            base_name = Path(filename).stem
            ext = "".join(Path(filename).suffixes)

        entry = Entry(
            abs_path=Path(dir_entry.path).absolute(),
            name=base_name,
            ext=ext[1:],
            type="file" if dir_entry.is_file() else "dir",
        )

        if entry_type == "all" \
            or (entry_type == "file" and entry.type == "file") \
            or (entry_type == "dir" and entry.type == "dir"):
                entries.append(entry)
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


print(list_entries("."))
