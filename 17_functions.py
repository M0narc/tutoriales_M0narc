# function = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")


hello("Bro", "Code", 21)


# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 8)

print(x)

# keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesn't matter, unlike positional arguments
#                       Python knows the names of the arguments that a function receives


def hello(first,middle,last):

    print("Hello "+first+" "+middle+" "+last)


hello(last="Code", middle="Dude", first="Bro")


# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function


# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)

# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))
