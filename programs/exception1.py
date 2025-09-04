### 1st approach : base class exception( default exception)
try:
    fobj = open("clients.txt","r")
    print(fobj.read())
except Exception as err:
    print(err)

# 2nd approach :  with multiple exceptions
try:
    fobj = open("clients.txt","r")
    print(fobj.read())
except TypeError as err:
    print("system error:",err)
    print("user defined error:Invalid opeartion")
except ValueError as err:
    print("system error:",err)
    print("user defined errror : invalid input")
except FileNotFoundError as err:
    print("file is not found")
    print(err)
except (IndexError,KeyError) as err:
    print("Invalid index or key")
    print("system error:", err)
except Exception as err:
    print(err)