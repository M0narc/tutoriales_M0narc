# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []  # create an empty list
for i in range(1, 11):  # create a for loop
    squares.append(i * i)  # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
# expression 1 * 1 for item (i) in our iterable(range)
squares = [i * i for i in range(1, 11)]
print(squares)

# using filter with LC
# first the lambda way
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# now the LC way
passe_students_lc = [i for i in students if i >= 60]
print(passe_students_lc)

# now the same LC with if/else statement

passe_students_lc = [i if i >= 60 else 'Failed' for i in students]
print(passe_students_lc)
