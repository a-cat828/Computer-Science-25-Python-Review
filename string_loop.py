word = input("Enter a word: ")
A = 0
for letter in word:
    print(letter)
    if letter == "a" or letter == "A":
        A = A+1
print(f"The letter a appears {A} times")