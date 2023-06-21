# Rock,paper,scissors

import random
def play():
    choose = input("choose any option to play. 'r' for Rock, 'p' for Paper and 's' for Scissors \n ").lower()
    computer = random.choice(['r', 'p', 's'])

    if choose == computer:
        return "Oh! It's a TIE"

    if win(choose, computer):
        return "Yay, You WON"

    return "you LOST"

# Inverted if function

    #if choose != computer:
        #if win(choose, computer):
            #return "Yay, you won"

        #return "You lost"

    #return "Oh!, It's Tie"


def win(user, machine):
    if(user == 'r' and machine == 's') or (user == 's' and machine == 'p') or (user == 'p' and machine == 'r'):
        return True

print(play())