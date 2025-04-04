import os
import platform
import shutil

if platform.system == "Windows":
    from colorama import just_fix_windows_console
    just_fix_windows_console()


def sort_entries(where: str) -> None:
    for entry in os.scandir(where):
        if entry.is_file():
            name, e = os.path.splitext(entry)
            ext: str = e[1:]
            exec_path: str = os.path.join(where, os.path.basename(__file__))
            if ext:
                if entry.path == exec_path:
                    continue
                elif entry.path != exec_path:
                    destination: str = os.path.join(where, ext.upper())
                    os.makedirs(destination, exist_ok=True)
                    try:
                        shutil.move(entry, destination)
                        print(f"{entry.path} moved to {destination}")
                    finally:
                        continue


if __name__ == "__main__":
    where_sort: str = input("Enter the path: ")
    sort_entries(where_sort)
