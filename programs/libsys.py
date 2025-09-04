
import sys

def version_platform_demo():
    # 1) Python version and platform
    print("version:", sys.version)
    print("version_info:", sys.version_info)
    print("platform:", sys.platform)

def path_getsizeof_demo():
    #Import search path and object sizes
    print("Size of 123(bytes):", sys.getsizeof(123))
    print("Size of 'python':", sys.getsizeof("python"))

version_platform_demo()
path_getsizeof_demo()
