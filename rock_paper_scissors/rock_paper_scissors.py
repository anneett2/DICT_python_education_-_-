import random

user_choice = input()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

if user_choice == computer_choice:
    print(f"There is a draw ({computer_choice})")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print(f"Well done. The computer chose {computer_choice} and failed")
elif user_choice in options:
    print(f"Sorry, but the computer chose {computer_choice}")
else:
    print("Invalid input")