import random

def play():
    user = input("What's ur chocie? 'r' for rock , 'p' for paper , 's' for scissors :\n")
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer:
        return "It\s a tie..!!"

    if winner(user, computer):
        return "You Won..!!"

    return "You Lost..!!"

def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

print(play())
