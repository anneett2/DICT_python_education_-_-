import random

name = input("Enter your name: ")
print(f"Hello, {name}")

# Читаємо рейтинг
score = 0
try:
    with open("rating.txt", "r") as f:
        for line in f:
            username, user_score = line.strip().split()
            if username == name:
                score = int(user_score)
except FileNotFoundError:
    pass

options = ["rock", "paper", "scissors"]

while True:
    user_input = input()

    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {score}")
    elif user_input not in options:
        print("Invalid input")
        continue

    computer_choice = random.choice(options)

    if user_input == computer_choice:
        score += 50
        print(f"There is a draw ({computer_choice})")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "scissors" and computer_choice == "paper") or \
         (user_input == "paper" and computer_choice == "rock"):
        score += 100
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")