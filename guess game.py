x = 25
a = int(input("Enter the number between 1 to 50: "))
if a < x and a <= 10:
    print("increase your number")
elif a < x and a > 10:
    print("increse litle more")
elif a > x and a >= 40:
    print("decrease your number ")
elif a > x and a < 40:
    print("decrease litle more")
elif a == x:
    print("Congratulation!!! \nyour guess is correct")

