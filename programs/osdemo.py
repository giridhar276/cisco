


import os
import time
import tempfile

# ---------- helpers ----------
def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

# ---------- examples (each in its own function) ----------
def ex01_getcwd():
    """[1] Current working directory"""
    print("\n[1] os.getcwd() -> current working directory")
    print("cwd:", os.getcwd())

def ex02_listdir():
    """[2] List current directory"""
    print("\n[2] os.listdir(path) -> list directory contents")
    print("Items in cwd:", os.listdir(os.getcwd()))

def ex03_makedirs(nested_dir):
    """[3] Create directories (makedirs)"""
    print("\n[3] os.makedirs(path, exist_ok=True) -> create folders")
    os.makedirs(nested_dir, exist_ok=True)  # creates parent chain as needed
    print("Created:", nested_dir, "exists?", os.path.isdir(nested_dir))

def ex04_create_file(file_path):
    """[4] Create a file and confirm existence"""
    print("\n[4] Create a file and check existence")
    write_text(file_path, "Hello from os demo!\n")
    print("Created:", file_path, "exists?", os.path.exists(file_path))

def ex05_rename(src, dst):
    """[5] Rename a file (os.rename)"""
    print("\n[5] os.rename(src, dst) -> rename/move file")
    os.rename(src, dst)
    print("Renamed to:", dst, "exists?", os.path.isfile(dst))

def ex06_remove_file(base_dir):
    """[6] Remove a file (os.remove)"""
    print("\n[6] os.remove(path) -> delete a file")
    tmp_for_delete = os.path.join(base_dir, "temp_delete.txt")
    write_text(tmp_for_delete, "This will be deleted.\n")
    print("Before remove exists?", os.path.exists(tmp_for_delete))
    os.remove(tmp_for_delete)
    print("After remove exists?", os.path.exists(tmp_for_delete))

def ex07_path_helpers(base_dir):
    """[7] Path helpers (join, basename, dirname, splitext)"""
    print("\n[7] os.path helpers: join / basename / dirname / splitext")
    joined = os.path.join(base_dir, "notes.txt")
    base_name = os.path.basename(joined)
    dir_name = os.path.dirname(joined)
    root, ext = os.path.splitext(joined)
    print("join ->", joined)
    print("basename ->", base_name)
    print("dirname  ->", dir_name)
    print("splitext ->", root, ext)

def ex08_abs_real_expanduser():
    """[8] Absolute & real paths + expanduser"""
    print("\n[8] abspath / realpath / expanduser")
    relative = "./"
    print("abspath(relative) ->", os.path.abspath(relative))
    print("realpath(relative)->", os.path.realpath(relative))
    print("expanduser('~')   ->", os.path.expanduser("~"))

def ex09_environment_vars():
    """[9] Environment variables"""
    print("\n[9] Environment variables via os.environ")
    home = os.environ.get("HOME") or os.environ.get("USERPROFILE")
    print("HOME/USERPROFILE:", home)
    os.environ["OS_DEMO_VAR"] = "123"
    print("Set OS_DEMO_VAR ->", os.environ.get("OS_DEMO_VAR"))
    os.environ.pop("OS_DEMO_VAR", None)
    print("Removed OS_DEMO_VAR ->", os.environ.get("OS_DEMO_VAR"))

def ex10_scandir(path):
    """[10] Efficient directory listing (os.scandir)"""
    print("\n[10] os.scandir(path) -> iterate directory entries")
    with os.scandir(path) as it:
        for entry in it:
            kind = "dir" if entry.is_dir() else "file" if entry.is_file() else "other"
            print(f" - {entry.name:<20} ({kind})")

def ex11_exists_isfile_isdir(base_dir, subdir, file_path):
    """[11] Existence & type checks"""
    print("\n[11] exists / isfile / isdir")
    print("base exists?", os.path.exists(base_dir), "isdir?", os.path.isdir(base_dir))
    print("subdir exists?", os.path.exists(subdir), "isdir?", os.path.isdir(subdir))
    print("file exists?", os.path.exists(file_path), "isfile?", os.path.isfile(file_path))

def ex12_walk(path):
    """[12] Walk a directory tree (os.walk)"""
    print("\n[12] os.walk(path) -> traverse directories")
    for root_dir, dirs, files in os.walk(path):
        print("ROOT:", root_dir)
        print("  dirs:", dirs)
        print("  files:", files)

def ex13_size_and_mtime(file_path):
    """[13] Size and modification time"""
    print("\n[13] getsize / getmtime")
    size = os.path.getsize(file_path)
    mtime = os.path.getmtime(file_path)
    print(f"Size of {os.path.basename(file_path)}:", size, "bytes")
    print("Modified time:", time.ctime(mtime))

def ex14_permissions_chmod(file_path):
    """[14] File permissions (chmod) — POSIX-only demo"""
    print("\n[14] os.chmod(path, mode) (POSIX-only example)")
    if os.name == "nt":
        print("Windows detected; skipping chmod demo (different permissions model).")
    else:
        before = os.stat(file_path).st_mode & 0o777
        os.chmod(file_path, 0o644)  # owner rw, group r, others r
        after = os.stat(file_path).st_mode & 0o777
        print("Before mode:", oct(before), "After mode:", oct(after))

def ex15_process_info_and_system():
    """[15] Process info & simple shell command"""
    print("\n[15] getpid / cpu_count / os.system")
    print("PID:", os.getpid(), "CPU count:", os.cpu_count())
    rc = os.system('echo "OS demo finished."')
    print("os.system return code:", rc)

# ---------- driver ----------
def main():
    print("== Python os module: 15 basic examples (each in its own def) ==\n")

    # Temporary sandbox auto-cleans on exit
    with tempfile.TemporaryDirectory() as base:
        subdir = os.path.join(base, "subdir")
        nested = os.path.join(subdir, "nested")
        file_a = os.path.join(base, "hello.txt")
        file_b = os.path.join(base, "greeting.txt")

        # call each example function
        ex01_getcwd()
        ex02_listdir()
        ex03_makedirs(nested)
        ex04_create_file(file_a)
        ex05_rename(file_a, file_b)
        ex06_remove_file(base)
        ex07_path_helpers(base)
        ex08_abs_real_expanduser()
        ex09_environment_vars()
        ex10_scandir(base)
        ex11_exists_isfile_isdir(base, subdir, file_b)
        ex12_walk(base)
        ex13_size_and_mtime(file_b)
        ex14_permissions_chmod(file_b)
        ex15_process_info_and_system()

    print("\nSandbox cleaned up. Done.")

if __name__ == "__main__":
    main()
