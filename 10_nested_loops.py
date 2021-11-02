# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"
# a nested loop is a general concept of having one loop inside of another loop

rows = int(input("How many rows? ->"))
columns = int(input("How many columns ->"))
symbol = input("Enter a symbol to use ->")

for i in range(rows):
    for j in range(columns):
        # if we don't use the end="" the next symbol will be in the next line
        print(symbol, end="")
    print()
