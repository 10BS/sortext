import os
from pathlib import Path
from typing import Literal

from data_classes import Entry


class Listing:
    @staticmethod
    def list_entries(
        path: str = ".",
        entry_type: Literal["all", "file", "dir"] = "all",
    ) -> list[Entry]:
        """
        Make listing of entries which contains in path
        :param path: which path to take when listing content
        :param entry_type: what type of content should be included in the list
        :return:
        """
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


def filter_entries() -> list[Entry]:
    pass

def check_signature() -> bool:
    pass

def fix_ext():
    pass
