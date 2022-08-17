# while loop =  a statement that will execute it's block of code,
#                        as long as it's condition remains true

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello "+name)

from unicodedata import name


min_length = 2

while True:
    name = input("Enter your name: ")
    if len(name) > min_length and name.isprintable() and name.isalpha():
        break
print(f"your name is {name}")


a = 0

while a < 10:
    a+=1
    if a % 2 == 0:
        continue
    print(a)
