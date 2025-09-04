import os

def cwd_demo():
    print("cwd:", os.getcwd())

def listdir_demo():
    print("Items in :", os.listdir("."))

def mkdir_demo():
    try:
        os.mkdir("demo_os_dir")
        print("Created folder:", "demo_os_dir")
    except FileExistsError:
        print("Folder already exists:", "demo_os_dir")

def create_file_demo():
    if not os.path.exists("hello.txt"):
        f = open("hello.txt", "w")
        f.write("Hello from os demo!\n")
        f.close()
    else:
        print("File already present:", "hello.txt")

def rename_file_demo():
    if os.path.exists("hello.txt"):
        # os.rename(old,new)
        os.rename("hello.txt", "greeting.txt")
    else:
        print("Nothing to rename; missing:", "hello.txt")

def exists_demo():
    # 7) Check if paths exist
    print("\n[7] os.path.exists(path)")
    print("Does", "demo_os_dir", "exist?", os.path.exists("demo_os_dir"))

def remove_file_demo():
    if os.path.exists("greeting.txt"):
        os.remove("greeting.txt")
        print("Removed file:", "greeting.txt")
    else:
        print("No file to remove at:", "greeting.txt")


cwd_demo()
listdir_demo()
mkdir_demo()
rename_file_demo()
exists_demo()
remove_file_demo()




