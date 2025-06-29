import sort
import os, shutil


if __name__ == "__main__":
    path = r".fleet"
    filtered = sort.filter_by_ext(path)
    for e in filtered:
        dst = os.path.join(path, e["ext"].upper())
        src = e["path"]
        os.makedirs(dst, exist_ok=True)
        shutil.move(src, dst)
    print("\nProcess finished with exit code 0")