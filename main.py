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


def mk_mv2dir(source, destination) -> None:
    os.makedirs(destination, exist_ok=True)
    shutil.move(source, destination)


def mv(where: str) -> None:
    for path in os.scandir(where):
        if path.is_file():
            root, ext = os.path.splitext(path)
            if ext[1:]:
                destination = os.path.join(where, ext[1:].upper())
                mk_mv2dir(path, destination)
                print(f"{path.path} moved to {destination}")


if __name__ == "__main__":
    path = input("Enter the path: ")
    mv(path)
