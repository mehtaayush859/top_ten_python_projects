import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry, guess again. Too low.") 
        elif guess > random_number:
            print("Sorry, guess again. Too high.") 

    print(f"Yes, you got it right..!!. The random number was {random_number}")

guess(20)