import random

# Defining True Num:
DataRange = list(range(0, 11))
TrueNum = int(random.choice(DataRange))
print("it`s in range from o to 10")

# Getting Guesses From User:
while True:
    try:
        Guess = int(input("Input your number: "))
        if Guess > TrueNum:
            print("You Are Getting Far...")

        elif Guess < TrueNum:
            print("It`s bigger than you think :)")
        elif Guess == TrueNum:
            print("yeah that`s it")
            break

    except ValueError:
        print("Invalid Choice")

