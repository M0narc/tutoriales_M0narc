# A decorator in Python is a function that takes another function as its argument, and returns
# yet another function . Decorators can be extremely useful as they allow the extension of an
# existing function, without any modification to the original function source code.
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value} ")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(10, 40))
