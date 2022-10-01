from itertools import count
import re
import operator

def to_jaden_case(string):
    """
    evry word capitilized
    """
    x = [i.title() for i in string.split(" ")]
    return " ".join(x)

def filter_list(x):
    """
    filter the numbers in the list
    """
    return list(filter(lambda x: type(x) == int, x))

def high_and_low(numbers):
    """
    takes a string, makes it a list, substract the highest and lowerst 
    number and returns it as a string
    """
    lis = numbers.split(" ")[::-1]
    num = [int(num) for num in lis]
    num.sort()
    l2 = [str(num[-1]), str(num[0])]
    return " ".join(l2)

def opposite(number):
    """
    takes a number and return the absolut number
    """
    return -abs(number) if number > 0 else abs(number)

def basic_op(ope, value1, value2):
    """
    import operator
    toma un operador y dos valores, devuelve el resultado
    """
    dic = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    return dic[ope](value1, value2)

def validate_pin(pin): 
    """
    validate that pin number is = to 4 or 6 positive numbers
    """
    return True if len(pin) == 4 and pin.isdigit() and int(pin) >= 0 or\
           len(pin) == 6 and pin.isdigit() and int(pin) >= 0 else False


def fake_bin(x):
    """
    import re, in order to find and substitute numbers of x and z lists
    """
    z = re.sub("[0-4]", "0", x)
    q = re.sub("[5-9]", "1", z)
    return q

def count_sheep(sheep):
    """
    just a counter
    """
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count

def count_sheep_2(sheep):
    """
    version 2.0 of a counter
    """
    return sheep.count(True)

def DNA_strand(dna):
    """
    uses the letters as reference for each character in the dna string
    """
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])

def dna_to_rna(dna):
    reference = {
        "T": "U",
        "G": "G",
        "C": "C",
        "A": "A"
    }
    return "".join([reference[x] for x in dna])

def dna_to_rna_2(dna):
    return dna.replace('T', 'U')

def average_of_three(a, b, c):
    average = int((a + b + c) / 3)
    if average >= 90 and average <= 100:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# def is_isogram(string):
#     for character in string:
#         print(string.count(character))
#         if string.count(character) > 1:
#             return False

def is_isogram(string):
    for character in string.lower():
        return False if string.count(character) > 1 else True