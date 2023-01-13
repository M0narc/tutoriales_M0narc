"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""

def number_lines(lines):
    numbered_lines = []
    for i, line in enumerate(lines):
        numbered_lines.append(f"{i+1}: {line}")
    return numbered_lines

print(number_lines(["a", "b", "c"]))
