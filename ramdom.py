import random


print("GUESS IT AGAIN")
r = random.randint(0, 100)

while True:
    i = int(input("Guess correct number: "))

    if r < i:
        print("less than guess ")
    elif r > i:
        print("greater than guess ")
    else:
        print("right")
        print("YOU WON")
        break
