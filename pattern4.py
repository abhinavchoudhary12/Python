a = int(input("Enter the number of rows: "))

for x in range(1, a+1):
    for y in range(1, a+1):
        print(y, end="")
    a -= 1
    print("\n")


