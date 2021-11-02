# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

# # we use break to gtfo of the while statement
# while True:
#     name = input("Enter your name")
#     if name != "":
#         break

# # if i == - we skip that iteration and print only the numbers + end="" makes it in only one line
# phone_number = "111-456-949"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# pass does... nothing, it acts as a placeholder
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i, end="")
