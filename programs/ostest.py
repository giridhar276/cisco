import os
# os name
print(os.name)

# present working directory
print("present working directory:",os.getcwd())

# create directory
dirname = "testdir"
if not os.path.isdir(dirname):
    os.mkdir("testdir")
else:
    print("dir already exists")

# display files and directories
print(os.listdir())

# delete directory
os.rmdir("testdir")

# display username
print(os.getlogin())

# display files and its size
for file in os.listdir():
    print(file.ljust(20),os.path.getsize(file),"bytes")