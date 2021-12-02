# Python threading tutorial
# ******************************************************
# thread =  a flow of execution. Like a separate order of instructions.
# each thread carries out it's own separated order of instruction in other words,
# each thread can run different parts of it's program at the same time
# they run concurrently but not truly in parallel
#                  each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# this makes the threads to synchronize
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


# --------- https://realpython.com/python-gil/ Point of reference ---------------
# about GIL The Python Global Interpreter Lock or GIL
# that allows only one thread to hold the control of the Python interpreter.
# This means that only one thread can be in a state of execution at any point in time.
# The impact of the GIL isn’t visible to developers who execute single-threaded programs,
# but it can be a performance bottleneck in CPU-bound and multi-threaded code

# What Problem Did the GIL Solve for Python?

# Python uses reference counting for memory management.
# It means that objects created in Python have a reference count variable
# that keeps track of the number of references that point to the object.
# When this count reaches zero, the memory occupied by the object is released.

# import sys
# a = []
# b = a
# sys.getrefcount(a)

# In the above example, the reference count for the empty list object [] was 3.
# The list object was referenced by a, b and the argument passed to sys.getrefcount().

# BACK TO GIL
# The problem was that this reference count variable needed protection from
# race conditions where two threads increase or decrease its value simultaneously.
# If this happens, it can cause either leaked memory that is never released or,
# even worse, incorrectly release the memory while a reference to that object still exists.
# This can cause crashes or other “weird” bugs in your Python programs.

