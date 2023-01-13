"""
The first century spans from the year 1 up to and including the year 100, the second century
- from the year 101 up to and including the year 200, etc.
Task
Given a year, return the century it is in.
"""
def century(year):
    year = str(year)  #
    return int(year[0:2]) if len(str(year)) > 3 else int(year[0:1])

print(century(200))
print(century(1200))
# s = "1400"
# print(s[0:2])

def c(y):
    "this is the one that actually works as intended"
    return int((y + 99) / 100)

print(c(201))
print(c(1201))