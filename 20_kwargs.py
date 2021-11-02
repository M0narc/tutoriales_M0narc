# **kwargs =   parameter that will pack all arguments into a dictionary
#                       useful so that a function can accept a varying amount of keyword arguments

# it's identical to *args except that *args accepts positional arguments and pack them into a tuple
# whilst **kwargs will accept a varying amount of keyword arguments and pack them into a dictionary

def hello(**kwargs):
    # in order to get the value within the dictionary, you need to write the name of the dic
    # and the key name, just like the comment below
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Bro", middle="Dude", last="Code")
