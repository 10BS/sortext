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


def create_dir(where) -> None:
    for name in list_exts(where):
        os.makedirs(os.path.join(where, str(name).upper()), exist_ok=True)


if __name__ == "__main__":
    path = input("Enter the path: ")
