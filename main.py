import os
import platform
import shutil
from os import DirEntry

from tinytag import TinyTag


def makedirs_movedirs(source: str | DirEntry, destination: str | DirEntry) -> None:
    os.makedirs(destination, exist_ok=True)
    shutil.move(source, destination)
    print(f"{source.path} moved to {destination}")


def list_entries(directory: str) -> list:
    entries = list()
    for entry in os.scandir(directory):
        basename, dot_ext = os.path.splitext(entry)
        ext: str = dot_ext[1:]
        entry_info = {
            "path": entry.path,
            "basename": basename,
            "ext": ext,
            "is_file": True if os.path.isfile(entry) else False,
            "is_dir": True if os.path.isdir(entry) else False,
        }
        entries.append(entry_info)

    return entries


def filter_entries(directory: str, entries: list | set, *exts: str) -> None:
    for entry in list_entries(directory):
        pass



def sort_entries(where: str) -> None:
    for entry in os.scandir(where):
        if entry.is_file():
            name, dot_ext = os.path.splitext(entry)
            ext: str = dot_ext[1:]
            exec_path: str = os.path.join(where, os.path.basename(__file__))
            print(entry.path)
            destination: str = os.path.join(where, ext.upper())
            if ext:
                if entry.path == exec_path:
                    continue
                elif entry.name in os.scandir(destination):
                    print("!")
                else:
                    makedirs_movedirs(entry, destination)


if __name__ == "__main__":
    path: str = input("Enter the path: ")
    print(list_entries(path))
