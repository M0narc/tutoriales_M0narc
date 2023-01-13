"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
"""
def double_char(s):
    return "".join(char * 2 for char in s)

print(double_char("Retard"))


def double_char_v2(string):
    double_string = ""
    for char in string:
        double_string += char + char
    return double_string
