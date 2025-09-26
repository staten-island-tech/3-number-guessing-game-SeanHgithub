import random
x = random.randint(1,10)
print("Guess a number 1-10")
guess_history = []
while True:
    guess = int(input("Enter a number"))
    if guess > x:
        print("Too high")
        guess_history.append(guess)
        print(guess_history)
    elif guess < x:
        print("too low")
        guess_history.append(guess)
        print(guess_history)
    elif guess == x:
        guess_history.append(guess)
        print(f"You got it! The number was {x}. You guessed {guess_history}")
        
        


