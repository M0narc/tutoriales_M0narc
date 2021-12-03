# slicing = create a substring by extracting elements from another string

#           indexing[] or slice()

#           [start:stop:step]


name = "Bro Code"

first_name = name[:3]  # [0:3]
print(first_name)

last_name = name[4:]  # [4:end]
print(last_name)

funky_name = name[::2]  # [0:end:2]
print(funky_name)

reversed_name = name[::-1]  # [0:end:-1]
print(reversed_name)

website1 = "http://google.com"

website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])

print(website2[slice])
