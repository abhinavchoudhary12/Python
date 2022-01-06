a = int(input("Enter the number of rows: "))
b = 0
for x in range(1, a+1):
    for y in range(1, x+1):

        b += 1
        print(b, end="")
    print("\n")


