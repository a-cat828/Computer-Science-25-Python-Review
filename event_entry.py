ticket = input("do you have a ticket(yes/no)")
age = int(input("how old are you?(number)"))

if ticket == "yes" and age >= 14:
    print("you can enter")
else:
    print("you can not enter")