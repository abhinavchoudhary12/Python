x = 25
count = 0
print("                               *******************************")
print("                               ** Welcome to the guess game **")
print("                               *******************************\n")
while count < 5:
    a = int(input("Enter the number between 1 to 50: "))
    if a < x and a <= 10:
        print("\nincrease your number\n")
        count += 1
    elif a < x and a > 10:
        print("\nincrease little more\n")
        count += 1
    elif a > x and a >= 40:
        print("\ndecrease your number \n")
        count += 1
    elif a > x and a < 40:
        print("\ndecrease little more\n")
        count += 1
    elif a == x:
        print("\nCongratulation!!! \nyour guess is correct")
        break;
if count == 5:
    print("you exceded the no. of guesses\ntry again")

