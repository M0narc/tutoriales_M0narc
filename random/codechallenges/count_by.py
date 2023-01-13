"""
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).
"""

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    lc = []
    for i in range(n):
        lc.append(x * i)
    return lc

# print(count_by(1, 10))
# print(count_by(2, 5))
# print(count_by(3, 5))

def count_by_v2(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x * i for i in range(1, n+1)]

print(count_by_v2(1, 10))
print(count_by_v2(2, 5))
print(count_by_v2(3, 5))