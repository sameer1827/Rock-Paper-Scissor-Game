import random

def get_choices():
    player_choice = input("Enter your choice (rock , paper, scissors):")
    options =["rock", "paper", "scissors"]
    computer_choice= random.choice(options)
    choices ={"player": player_choice , "computer":computer_choice}
    return choices

def check_win(player , computer):
    print(f"You choose {player} , computer choose {computer}  ")
    if player == computer:
        return "It's a tie match"
    elif player== "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win ! "
        else:
             return "Paper covers rock , You lose. "
    elif player== "paper":
        if computer == "rock":
            return "Papers covers rock ! You win! "
        else:
             return "Scissors cuts paper , You lose."

    elif player== "scissors":
        if computer == "paper":
            return " scissors cuts paper! You win ! "
        else:
             return "rock smashes scissors, You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

