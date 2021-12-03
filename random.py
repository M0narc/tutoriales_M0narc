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
#
#
# def das(n):
#     # lis = sorted(n.split(" ")[::-1])
#     num = [int(i) for i in n.split()]
#     return f"{max(num)} {min(num)} "
#
#
# string = "-1 -22 43 74 5"
# print(das(string))
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
import operator


def basic_op(ope, x, y):
    o = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    return o[ope](x, y)

print(basic_op("+", 6, 6))
