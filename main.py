import os
import shutil
from typing import Literal


def list_entries(
    path: str = ".", type: Literal["all", "file", "dir"] = "all"
) -> list[dict[str, str | bool]]:
    entries: list = []
    for e in os.scandir(path):
        basename, dot_ext = os.path.splitext(e.name)
        ext: str = dot_ext[1:]
        entry = {
            "path": os.path.abspath(e),
            "name": basename,
            "ext": ext,
            "is_file": True if os.path.isfile(e) else False,
            "is_dir": True if os.path.isdir(e) else False,
        }
        if type == "all":
            entries.append(entry)
        elif type == "file":
            entries.append(entry) if entry.get("is_file") else None
        elif type == "dir":
            entries.append(entry) if entry.get("is_dir") else None

    return entries


def filter_by_ext(path: str, *pool_ext):
    filtered = []
    for e in list_entries(path, "file"):
        if e["ext"] in pool_ext:
            filtered.append(e)

    return filtered


if __name__ == "__main__":
    path = r"Y:\Downloads\Telegram Desktop"
    filtered = filter_by_ext(path, "mov", "py", "flac", "MP4", "mp4")
    for e in filtered:
        dst = os.path.join(path, e["ext"].upper())
        src = e["path"]
        os.makedirs(dst, exist_ok=True)
        shutil.move(src, dst)
    print("\nProcess finished with exit code 0")