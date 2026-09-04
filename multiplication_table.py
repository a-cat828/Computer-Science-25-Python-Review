numb = int(input("enter what multiplication table you want? "))
max = (numb * 10) + numb
for number in range(numb,max,numb):
    print(number)