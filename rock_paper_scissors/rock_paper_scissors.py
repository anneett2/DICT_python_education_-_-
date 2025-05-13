import random

def get_win_map(options):
    win_map = {}
    length = len(options)
    for idx, item in enumerate(options):
        defeats = options[idx+1:] + options[:idx]
        half = len(defeats) // 2
        win_map[item] = defeats[:half]
    return win_map

name = input("Enter your name: ")
print(f"Hello, {name}")

# Отримуємо рейтинг
score = 0
try:
    with open("rating.txt", "r") as f:
        for line in f:
            username, points = line.strip().split()
            if username == name:
                score = int(points)
except FileNotFoundError:
    pass

# Отримуємо опції гри
options_input = input()
options = options_input.split(",") if options_input else ["rock", "paper", "scissors"]
print("Okay, let's start")

win_map = get_win_map(options)

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
    elif computer_choice in win_map[user_input]:
        score += 100
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")