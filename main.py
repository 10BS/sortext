import os
import platform
import shutil

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


def make_dirs(where: str, exts: set = None) -> None:
    exts = list_exts(where)
    for ext in exts:
        os.makedirs(ext.upper(), exist_ok=False)


def move(source: str, destination: str) -> None:
    for entry in os.scandir(source):
        shutil.move(entry, f"./{destination}")


if __name__ == "__main__":
    path = input("Enter the path: ")
    exts = list_exts(path)
    make_dirs(path, exts)
