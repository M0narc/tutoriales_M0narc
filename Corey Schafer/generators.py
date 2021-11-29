# Python Generator functions allow you to declare a function that behaves likes an iterator
# An iterator is an object that can be iterated or looped upon. It
# is used to abstract a container of data to make it behave like an iterable object

# the reason we use generators over lists is that it is much more readable
# instead of having a new list, appending the result and returning
# we YIELD each item just ONCE and that's it

# the lines commented are the ones we're supposed to use if this was a for loop
# and not a generator
def square_numbers(nums):
    # result = [] we don't need to instantiate the list
    for i in nums:
        yield (i*i)  # result.append(i*i) is the for loop way
    # return result we don't need the return since we're using the yield


my_nums = square_numbers([1, 2, 3, 4, 5])
# my_nums = [x*x for x in [1, 2, 3, 4, 5]] # this is a list comprehension
                                           # it does the same thing as the def above if it was a for loop
# my_nums = (x*x for x in [1, 2, 3, 4, 5]) # AND THIS is the way to have it as a generator, we switch the [] for ()

print(my_nums.__next__())  # prints [1, 4, 9, 16, 25]
# you can cast this generator into a list but it loses it's purpose of being a
# generator that actually helps performance
