import os
import platform
import shutil
from os.path import splitext


if platform.system == "Windows":
    from colorama import just_fix_windows_console
    just_fix_windows_console()


def list_exts(directory: str) -> set:
    exts = set()
    for p in os.scandir(directory):
        if p.is_file():
            root, ext = os.path.splitext(p)
            exts.add(ext[1:]) if ext else ""
    return exts


def create_move(where: str) -> None:
    for name in list_exts(where):
        neue_folder = os.path.join(where, str(name).upper())
        os.makedirs(neue_folder, exist_ok=True)
        for entry in os.scandir(where):
            full_path_entry = entry.path
            if entry.is_file():
                shutil.move(full_path_entry, neue_folder)


if __name__ == "__main__":
    path = input("Enter the path: ")
    create_move(path)
