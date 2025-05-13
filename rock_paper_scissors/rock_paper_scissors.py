user_choice = input()

# Мапа перемог
win_map = {
    "rock": "paper",
    "scissors": "rock",
    "paper": "scissors"
}

if user_choice in win_map:
    computer_choice = win_map[user_choice]
    print(f"Sorry, but the computer chose {computer_choice}")
else:
    print("Invalid input")
