# guess the number (computer guessing)
import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            pick = random.randint(low, high)
        else:
            pick = high
        feedback = input(f"Is {pick}  is too high [h] or too low [l] or it is correct [c]: ").lower()
        if feedback == "h":
            high = pick - 1
        elif feedback == "l":
            low = pick + 1

    print(f"yay, computer guessed number {pick} correctly ")


computer_guess(1000)