# explicit line continuation
a = [1, 2, 3]
a = [1, 2
    ,3]
print(a)

a = [1, #item 1
    2]


def my_fun(a, # comment
           b, # comment
           c # comment
           ):
    print(a, b, c)

############################

# next we use a line continuation character
a = 10
b = 20
c = 30
if a > 5\
    and b > 10\
        and c > 20:
    print('drinking is yes')
# triple delimeter
a = '''this is a string'''