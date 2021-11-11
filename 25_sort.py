# sort() method   = is a built in method for LISTS
# sort() function = is used with iterables, it returns a sorted list from other iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))


grade = lambda grades: grades[1]
# students.sort(key=age) # tambien puede usar  reverse=True # sorts current list
sorted_students = sorted(students, key=grade)  # sorts and creates a new list from that other iterable(the tuple)

for i in sorted_students:
    print(i)
