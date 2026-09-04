num = 6
number = int(input("Enter a number from 1 to 10: "))

while number != num:
    while number > num:
        print("too big")
        number = int(input("Enter a number from 1 to 10: "))
    while number < num:
        print("too small")
        number = int(input("Enter a number from 1 to 10: "))
print(f"You did it!!!")
