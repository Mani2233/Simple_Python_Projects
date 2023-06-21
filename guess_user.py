# Guess the number(user guessing)
import random


def guess(x):
    random_number = random.randint(1, x)
    my_guess = 0
    while my_guess != random_number:
        my_guess = int(input(f"please enter number between 1, {x}: "))
        if my_guess < random_number:
            print("your guess is too low  , try again")
        elif my_guess > random_number:
            print("your guess is too high  , try again")

    print(f"congrats, you have guessed number {random_number} correctly")


guess(10)