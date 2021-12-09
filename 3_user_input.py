name = input("What is your name?: ")

# age = int(input("How old are you?: "))

# height = float(input("How tall are you?: "))
x = True
while x == True:

    print("Hello " + name)
    n = input("if that's your name, write yes ")
    if n in ("y", "yes", "yeah"):
        x = False
    else:
        name = input("write your name again ")

# print("You are " + str(age) + " years old")

# print("You are " + str(height) + "cm tall")
