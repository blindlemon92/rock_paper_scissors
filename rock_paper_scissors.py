import random

# Have fun!!

def game(selection=""):
    choices = [ 'rock', 'paper', 'scissors']
    computer_selection = random.choice(choices)
    user_selection = input('\nrock, paper, or scissors? ')
    if user_selection == computer_selection:
        print (f"\nYour computer adversary chose: {computer_selection} - Game Tied")
    elif user_selection == 'rock' and computer_selection == "paper":
        print(f"\nYour computer adversary chose: {computer_selection} - You Lose")
    elif user_selection == 'paper' and computer_selection == "scissors":
        print(f"\nYour computer adversary chose: {computer_selection} - You Lose")
    elif user_selection == 'scissors' and computer_selection == "rock":
        print(f"\nYour computer adversary chose: {computer_selection} - You Lose")
    else:
        print(f"\nYour computer adversary chose: {computer_selection} - You Win!")


def run():
    key = 1
    while key:
        value = input("\nYou wanna play rock, paper, scissors? (y to play, n to not) ")
        if value == "y":
            game()
        elif value == "n":
            key = 0

run()
    
