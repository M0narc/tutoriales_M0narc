utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()

# update is used in order to append another set
dishes.update(utensils)
# joins to sets together and create a new set entirely
dinner_table = utensils.union(dishes)

# this compares what utensils has, that dishes doesn't
print(dishes.difference(utensils))
# what do this sets have in common can be seeing using intersection
print(utensils.intersection(dishes))

for x in utensils:
    print(x, end=" ")
