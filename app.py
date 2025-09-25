import random
x = random.randint(1,10)
print("Guess a number 1-10")
guess = int(input("Enter a number"))
while True:
    if guess != x:
        print("Guess again")
    else:
        break


