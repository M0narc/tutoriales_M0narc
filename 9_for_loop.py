# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited
import time

# using range
# for i in range(10):
#     print(i)
#
# # count from one number to another from 50 to 99 in this case, since the second param is exclusive
# # and the third param tells it how by how many numbers you want to count, in this case, two
# for i in range(50, 100, 2):
#     print(i)

# # this will run each letter in the given param
# for i in "Franco":
#     print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("10 seconds have passed")
