# e = []
# x = ["Peter"]  # -->  "Peter likes this"
# z = ["Jacob", "Alex"]  # -->  "Jacob and Alex like this"
# q = ["Max", "John", "Mark"]  # -->  "Max, John and Mark like this"
# r = ["Alex", "Jacob", "Mark", "Max"]  # -->  "Alex, Jacob and 2 others like this"
#
#
# def likes(names):
#     if 0 < len(names) < 2:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     elif len(names) > 3:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
#     else:
#         return 'no one likes this'
#
#
# print(likes(r))

# --------------------------------------------
# def sad(n):
#     nn = [int(s) for s in n.split(" ")]
#     return "%i %i" % (max(nn), min(nn))

# def l(n):
#     return [int(i) for i in n.split()]

# def das(n):
#     # lis = sorted(n.split(" ")[::-1])
#     num = [int(i) for i in n.split()]
#     return f"{max(num)} {min(num)}"


# string = "-1 -22 43 74 5"
# print(sad(string))
# ---------------------------------------------

# # replacing characters in a string
# def DNA_strand(dna):
#     dic = {
#         'A': 'T',
#         'T': 'A',
#         'C': 'G',
#         'G': 'C'
#     }
#     return dna.translate(str.maketrans(dic))
#
# def DNA_strand(dna):
#     reference = { "A":"T",
#                   "T":"A",
#                   "C":"G",
#                   "G":"C"
#                   }
#     return "".join([reference[x] for x in dna])
#
#
# print(DNA_strand("AAAA"))
# print(DNA_strand("ATTGC"))
# print(DNA_strand("GTAT"))

# ---------------------------------------------------

# def valid_pin(pin):
#     """
#     Valid pin for card in ATM must be 4 or 6 digits, only numbers and it can't
#     contain negative numbers
#     :param pin:
#     :return:
#     """
#     return True if len(pin) == 4 and pin.isdigit() and int(pin) >= 0\
#                    or len(pin) == 6 and pin.isdigit() and int(pin) >= 0 else False
#
#
# def someone_else(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
#
#
# # print(valid_pin("123124"))
# # print(valid_pin("1234"))
# # print(valid_pin("12345"))
# # print(valid_pin("123"))
# # print(valid_pin("qwewq32"))
# # -----
# print(someone_else("-12323"))
# -----------------------------------------------------------------------

# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7
# import operator


# def basic_op(ope, x, y):
#     o = {
#         "+": operator.add,
#         "-": operator.sub,
#         "*": operator.mul,
#         "/": operator.truediv,
#     }
#     return o[ope](x, y)

# print(basic_op("+", 6, 6))

# -----------------------------------------------------------------
# el final del string tiene que ser igual
# import re

# def solution(string, ending):
#     return True if re.findall(f"{ending}$", string) else False

# print(solution("abc", "bc"))
# print(solution("samurai", "ra"))

# --------------------------------------------------------------------
# capitalize every word from a string
# first my way
# def to_jaden_case(string):
#     x = [i.capitalize() for i in string.split(" ")]
#     return " ".join(x)

# print(to_jaden_case("Something strange should happen"))
# # second way

# import string

# def cap_words(s):
#     return string.capwords(s)

# print(cap_words("Something strange should happen"))

# -------------------------------------------------------------------------

# # filter the numbers in the list
# def filter_list(x):
#     return list(filter(lambda x: type(x) == int, x))

# print(filter_list([1,2,'a','b', 4]))

# -------------------------------------------------------------------------

# sum and return the binary valor in a STRING

# from typing import BinaryIO


# def bin_sum(a,b):
#     c = a + b
#     return f"{c:b}"

# print(bin_sum(2,2))

# -------------------------------------------------------------------------

# pseudo encrypt something
"""
Implement a pseudo-encryption algorithm which given a string S and
an integer N concatenates all the odd-indexed characters of S with 
all the even-indexed characters of S, this process should be repeated N times.
"""
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

# """
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.
# """
# def decrypt(encrypted_text, n):
#     pass

# def encrypt_text(text, n):
#     pass


# import math

# def find_next_square(sq):
#     x = math.sqrt(sq)
#     if int(x + 0.5) ** 2 == sq:
#         new_perfect_square = sq + 1
#         new_x = math.sqrt(new_perfect_square)
#         w_switch = (int(new_x + 0.5) ** 2 == new_perfect_square)
#         while w_switch == False: 
#             new_perfect_square += 1
#             new_x = math.sqrt(new_perfect_square) 
#             w_switch = (int(new_x + 0.5) ** 2 == new_perfect_square)
#             if w_switch:
#                 break
#         return new_perfect_square
#     else:
#         return -1


# def test(sq):
#     root = math.sqrt(sq)
#     print(int(root + 0.5) ** 2 == sq)
#     if int(root + 0.5) ** 2 == sq:
#         print(sq, "is a perfect square")
#     else:
#         print(sq, "is not a perfect square")


# #t = test(121)


# f = find_next_square(121)
# print(f)

# # easier way
# def find_next_square(sq):
#     sqr = sq ** 0.5
#     print(sqr)
#     if sqr.is_integer():
#         return (sqr + 1) ** 2
#     return -1

# l = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]

# def find_needle(list):
#     return list.index('needle')

# print(find_needle(l))

# def opposite(n):
#     return -abs(n)

# print(opposite(26))

# from re import X


# num_list = [2, 3 , 4 , 3.67, 9]

# def sum_l(a):
#     suma_de_todo = 0
#     for num in a:
#         suma_de_todo = suma_de_todo + num
#     return suma_de_todo

# print(sum_l(num_list))

# l_score = [100, 40, 34, 57, 29, 72, 57, 88]

# def av_escore(l, mine):
#     av = sum(l) / len(l)
#     return mine > av

# print(av_escore(l_score, 80))
# import re

# st = "45385593107843568"
# def fake_bin(x):
#     z = re.sub("[0-4]", "0", x)
#     q = re.sub("[5-9]", "1", z)
#     return q

# txtdsa = fake_bin(st)
# print(txtdsa)

# from string import *
# def fake_bin2(x):        
#     return x.translate(str.maketrans('123456789', '006011111'))
    

# txtsad = fake_bin2(st)
# print(txtsad)

# def fake_bin3(x):
#     return ''.join('0' if c < '5' else '1' for c in x)

# st = "a b c d"

# def reverse_txt(txt):
#     """
#     reverse text
#     """
#     return txt[::-1]

# print(reverse_txt(st))

