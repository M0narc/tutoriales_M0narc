def add_list_to_specific_index(l1, l2):
    iterations = 0
    insert_in = 2
    from_index = 0
    while iterations < 6:
        l1[iterations:iterations] = l2[from_index:from_index+2]
        iterations += 2
        insert_in += 2
        print(insert_in)
        from_index += 2
        print(from_index)
        print(l1)


lis = [1, 2, 3, 4, 5, 6]
lis2 = ["a", "b" , "c", "d", "e", "f"]

add_list_to_specific_index(lis,lis2)
