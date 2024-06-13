import random


def binarySearch():
    x = int(input("Starting number : "))
    y = int(input("End number : "))
    guessed_number = random.randint(x,y)
    midNumber = 0;

    while(guessed_number != midNumber):
        midNumber = int((y + x) / 2)
        if midNumber > guessed_number:
            print(midNumber, " is Too high")
            y = midNumber - 1
        else:
            print(midNumber, "is too low")
            x = midNumber + 1

    print("I got the number and its ", midNumber)
    print("The guessed number was" , guessed_number)


binarySearch()