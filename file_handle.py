"""
FILE I/O
'w' -> Write-only mode
'r' -> Read-only mode
'r+'-> Read and write mode
'a' -> Append mode
"""

my_list = [1, 2, 3]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()


print("With as write start")
with open("firstfile.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as read/write")
print()
print("with as read start")
with open("firstfile.txt", "r") as with_as_read:
    print(str(with_as_read.read()))
