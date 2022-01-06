print("chose the Operation")
print("1 addition")
print("2 subtraction")
print("3 division")
print("4 multiplication")
operation = int(input("Enter the operation value: "))
if operation == 1:
    a = int(input("Enter value a: "))
    b = int(input("Enter value b: "))
    if a == 56 and b == 9:
        print("77")
    else:
        print(a+b)
elif operation == 2:
    a = int(input("Enter value a: "))
    b = int(input("Enter value b: "))
    print(a-b)
elif operation == 3:
    a = int(input("Enter value a: "))
    b = int(input("Enter value b: "))
    if a == 56 and b == 6:
        print("4")
    else:
        print(a/b)
elif operation == 4:
    a = int(input("Enter value a: "))
    b = int(input("Enter value b: "))
    if a == 45 and b == 3 or a == 3 and b == 45:
        print("555")
    else:
        print(a*b)
else:
    print("Enter the correct value")
