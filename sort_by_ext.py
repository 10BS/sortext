import os
import glob
import pathlib
import shutil


def sort(directory):
    for file_path in glob.glob(os.path.join(directory, '*')):
        if os.path.isfile(file_path):
            try:
                file_ext = pathlib.Path(file_path).suffix
                if file_ext:
                    target_dir = os.path.join(directory, file_ext.upper().replace('.', ''))
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, target_dir)
                    print(f"MOVED {file_path} TO {target_dir}")
                elif not file_ext:
                    continue
            except Exception as e:
                print(f"FAILED TO MOVE {file_path}: {e}")


if __name__ == "__main__":
    directory = input('DIR TO SORT: ')
    sort(directory)
