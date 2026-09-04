num_num = int(input("how many numbers? "))
for i in range(num_num):
    number = int(input("what is one of the numbers?"))
    if number > 0:
        print("it is positive")
        if number % 2 == 0:
            print("even")
        else:
            print("odd")
    elif number < 0:
        print("it is negative")
        if number % 2 == 0:
                print("even")
        else:
                print("odd")

    else:
        print("it is zero")
print(f"your {num_num} numbers have been Analyzed")