import os
import glob
import pathlib
import shutil


# Create a folder for the directories and move them to the created folder
def makedir_for_file(target_dir, file_path):
    os.makedirs(target_dir, exist_ok=True)
    shutil.move(file_path, target_dir)


# Create a folder for the files and move them to the created folder
def makedir_for_dir(target_dir, folder):
    os.makedirs(target_dir, exist_ok=True)
    shutil.move(folder, target_dir)


# Function for sorting files into folders named by the extension of the files to be sorted
def sort_files(directory):
    # Iterate the paths to all objects in the given directory to sort them
    for path in glob.glob(os.path.join(directory, "*"), include_hidden=True):
        # If the path in the loop is a file -- continue
        if os.path.isfile(path):
            # Try it. Select the file extension from the full file name
            try:
                file_ext = pathlib.Path(path).suffix
                ext = file_ext.upper().replace(".", "")
                file_name = pathlib.Path(path).stem

                # If the file starts with a dot or the file has no extension,
                # create a folder to sort it in called !HIDDEN and
                # move it there.
                if file_name.startswith(".") or not file_ext:
                    target_dir = os.path.join(directory, "!HIDDEN")
                    makedir_for_file(target_dir, path)
                    print(
                        f"HIDDEN / BLANK FILES {file_name}{file_ext} MOVED TO {target_dir}"
                    )

                # Also if a file has an extension, create a folder for it
                # Sort it by the name of its extension and move it there
                elif file_ext:
                    target_dir = os.path.join(directory, ext)
                    makedir_for_file(target_dir, path)
                    print(f"FILE {file_name}{file_ext} MOVED TO {target_dir}")

            # If for some reason the file could not be moved to the folder created for it
            # the folder created for it -- print an exception line and also label
            # the file name and extension
            except Exception as e:
                print(f"FAILED TO MOVE {file_name}{file_ext} -- {e}")


# Function for sorting directories into a folder named DIRS
def sort_dirs(directory):
    # Iterate the paths to all objects in the given directory to sort them
    for path in glob.glob(os.path.join(directory, "*"), include_hidden=True):
        # If the path in the loop is a directory -- continue
        if os.path.isdir(path):
            # Try it. Assign to the folder variable the full path to the directory
            try:
                folder = pathlib.Path(path)
                # If the loop object is a folder -- continue.
                # Create a folder named DIRS and move the directory there
                if folder:
                    target_dir = os.path.join(directory, "DIRS")
                    makedir_for_dir(target_dir, folder)
                    print(f"DIR {folder.stem} MOVED TO {target_dir}")
            # If for some reason the directory could not be moved to the folder created for it
            # folder created for it -- display an exception line and also indicate
            # directory name
            except Exception as e:
                print(f"FAILED TO MOVE {folder.stem} -- {e}")


if __name__ == "__main__":
    directory = input("DIR FOR SORT (WITHOUT QUOTES): ")
    q_sort_dirs = input("SORT DIRS? (Y/N): ")
    if q_sort_dirs.lower() == "y":
        sort_dirs(directory)
    else:
        pass
    sort_files(directory)
