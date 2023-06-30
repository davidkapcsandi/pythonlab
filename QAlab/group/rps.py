# Make a rock paper scissors app that I can play against the computer. 
# The program should keep track of the number of rounds played, the number of rounds
# won by the user, and the number of rounds won by the computer. 
# After each round, the program should display the results 
# and ask the user if they want to play another round. 
# You should use functions, loops, conditionals, random number generation to achieve this.

import random, sys

options = {1: "rock", 2: "paper", 3: "scissors"}

def rock_paper_scissors_game(computer_wins, human_wins, ):

    print(f"{options}\n")
    user_chosen = int(input("What do you wanna choose?"))
    print(f"The user has chosen: {options[user_chosen]}")

    computer_chosen = random.randint(1,3)
    print(f"The computer has chosen {options[computer_chosen]}")

    if user_chosen == 1:
        if computer_chosen == 3:
            human_wins += 1
            print("user")
        else:
            computer_chosen == 2
            computer_wins += 1
    elif user_chosen == 3:
        if computer_chosen == 2:
            human_wins += 1
            print("user")
        else: 
            computer_chosen == 1
            computer_wins += 1
            print("computer")

    else:
        user_chosen == computer_chosen
        print("draw")

   

while True:
    rounds_played = 0
    human_wins = 0
    computer_wins = 0
    play_answer = input("Do you want to play?")
    if play_answer == "yes":
        rounds_played += 1
        rock_paper_scissors_game(computer_wins, human_wins)
    else:
        sys.exit()