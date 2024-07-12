import os
import glob
import pathlib
import shutil


def makedir_for_file(target_dir, file_path):
    os.makedirs(target_dir, exist_ok=True)
    shutil.move(file_path, target_dir)


def makedir_for_dir(target_dir, folder):
    os.makedirs(target_dir, exist_ok=True)
    shutil.move(folder, target_dir)


def sort_files(directory):
    for path in glob.glob(os.path.join(directory, '*'), include_hidden=True):
        if os.path.isfile(path):
            try:
                file_ext = pathlib.Path(path).suffix
                ext = file_ext.upper().replace('.', '')
                file_name = pathlib.Path(path).stem

                if file_name.startswith('.') or not file_ext:
                    target_dir = os.path.join(directory, '!HIDDEN')
                    makedir_for_file(target_dir, path)
                    print(f"HIDDEN / BLANK FILES {file_name}{file_ext} MOVED TO {target_dir}")

                elif file_ext:
                    target_dir = os.path.join(directory, ext)
                    makedir_for_file(target_dir, path)
                    print(f"FILE {file_name}{file_ext} MOVED TO {target_dir}")

            except Exception as e:
                print(f"FAILED TO MOVE {file_name}{file_ext} -- {e}")


def sort_dirs(directory):
    for path in glob.glob(os.path.join(directory, '*'), include_hidden=True):
        if os.path.isdir(path):

            try:
                folder = pathlib.Path(path)
                if folder:
                    target_dir = os.path.join(directory, 'DIRS')
                    makedir_for_dir(target_dir, folder)
                    print(f"DIR {folder.stem} MOVED TO {target_dir}")

            except Exception as e:
                print(f"FAILED TO MOVE {folder.stem} -- {e}")


if __name__ == "__main__":
    directory = input('DIR FOR SORT (WITHOUT QUOTES): ')
    q_sort_dirs = input('SORT DIRS? (Y/N): ')
    if q_sort_dirs.lower() == 'y':
        sort_dirs(directory)
    else:
        pass
    sort_files(directory)
