import os

# if you have back slashes (\) you need to use two, cuz that's the escape sequence for a \ within a string
path = "C:\\Users\\User\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):         # this will let you know if it's a file
        print("That is a file")
    elif os.path.isdir(path):       # this will let you know if it's a folder/directory
        print("That is a directory!")
else:
    print("That location doesn't exist!")
