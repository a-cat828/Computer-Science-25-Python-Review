number = int(input("Enter a number from 1 to 100: "))

while number < 0 or number > 101:
    print("Invalid number.")
    number = int(input("Enter a number from 1 to 100: "))

print(f"You entered {number}.")