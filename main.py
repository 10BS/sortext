import os
import platform
import shutil
from os import DirEntry

if platform.system == "Windows":
    from colorama import just_fix_windows_console
    just_fix_windows_console()


def sort_entries(where: str) -> None:
    for entry in os.scandir(where):
        if entry.is_file():
            name, _ext = os.path.splitext(entry)
            ext = _ext[1:]
            exec_path = os.path.join(where, os.path.basename(__file__))
            if ext:
                if entry.path == exec_path:
                    continue
                elif entry.path != exec_path:
                    destination = os.path.join(where, ext.upper())
                    os.makedirs(destination, exist_ok=True)
                    shutil.move(entry, destination)
                    print(f"{entry.path} moved to {destination}")


if __name__ == "__main__":
    where = input("Enter the path: ")
    sort_entries(where)
