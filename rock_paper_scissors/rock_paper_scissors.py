import random

options = ["rock", "paper", "scissors"]

while True:
    user_input = input()

    if user_input == "exit" or "q":
        print("Bye!")
        break
    elif user_input not in options:
        print("Invalid input")
        continue

    computer_choice = random.choice(options)

    if user_input == computer_choice:
        print(f"There is a draw ({computer_choice})")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "scissors" and computer_choice == "paper") or \
         (user_input == "paper" and computer_choice == "rock"):
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")
