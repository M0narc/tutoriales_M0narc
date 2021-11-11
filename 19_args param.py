# *args =   parameter that will pack all arguments into a tuple
#                 useful so that a function can accept a varying amount of arguments


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8))


# args can be named potato if you want, you need the * for this to work
def dad(*stuff):
    sum = 0
    stuff = list(stuff)  # tuples can't be modified, cast it into a list if you want
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(dad(1, 2, 3, 4, 5, 6, 7, 8))
