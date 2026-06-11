# write "hello world" to the console
print("hello world")

# we are designing a mini-game of rock paper scissors based on three rules:
# rock beats scissors
# scissors beats paper
# paper beats rock

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The mini-game must handle user inputs, putting them in lowercase only and informing the user if the option is invalid.
# Make the game multiplayer, where the computer will be my opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move,
# just like I would. The computer's choice should be displayed to the player after each round.
# The game should keep track of the player's score and the computer's score, and display them at the end of each round. 
# The player should be able to choose to play again or exit the game after each round.
# User inputs should be in lowercase only and the game should handle invalid inputs gracefully by prompting the user to enter a valid option 
# for example if their input is uppercase or mixed case.
# The mini-game should display the scores, informing me of the number of wins and total rounds played at the end of the game.

import random                               
def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"
def play_game():
    player_score = 0
    computer_score = 0
    while True:
        raw_choice = input("Enter rock, paper, or scissors (lowercase only): ")
        if raw_choice != raw_choice.lower():
            print("Please enter your choice in lowercase only.")
            continue
        player_choice = raw_choice
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        while True:
            raw_again = input("Do you want to play again? (yes/no) (lowercase only): ")
            if raw_again != raw_again.lower():
                print("Please answer in lowercase only ('yes' or 'no').")
                continue
            play_again = raw_again
            if play_again in ["yes", "no"]:
                break
            print("Invalid response. Please enter 'yes' or 'no'.")
        if play_again != "yes":
            break
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")
play_game()     

