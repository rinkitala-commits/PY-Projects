import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {
    ROCK : "🪨",
    PAPER : "📃",
    SCISSORS : "✂️"
}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice")

def display_choices(user_choice, computer_choice):
     print(f"You chose {emojis[user_choice]}")
     print(f"Computer chose {emojis[computer_choice]}")
     
def determine_winer(user_choice, computer_choice):
    if user_choice == computer_choice :
        print("It's a tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)) :
            print("You Win!")
    else :
        print("You Lose!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winer(user_choice, computer_choice)

        ask = input("Continue? (y / n) :").lower()
        if ask == "n" :
            print("Thanks for playing !!")
            
            break
        
play_game()