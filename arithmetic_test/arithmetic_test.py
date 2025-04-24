import random

def simple_quiz():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    op = random.choice(['+', '-', '*'])
    print(f"{a} {op} {b}")
    return eval(f"{a}{op}{b}")

def square_quiz():
    a = random.randint(11, 29)
    print(a)
    return a ** 2

while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level = input()
    if level in ['1', '2']:
        level = int(level)
        break
    else:
        print("Incorrect format.")

correct = 0
for _ in range(5):
    if level == 1:
        answer = simple_quiz()
    else:
        answer = square_quiz()
    while True:
        user_input = input()
        try:
            if int(user_input) == answer:
                print("Right!")
                correct += 1
            else:
                print("Wrong!")
            break
        except ValueError:
            print("Incorrect format.")

print(f"Your mark is {correct}/5.")

print("Would you like to save your result to the file? Enter yes or no.")
save = input()
if save.lower() in ['yes', 'y']:
    print("What is your name?")
    name = input()
    if level == 1:
        level_description = "simple operations with numbers 2-9"
    else:
        level_description = "integral squares of 11-29"
    with open("results.txt", "a") as f:
        f.write(f"{name}: {correct}/5 in level {level} ({level_description})\n")
    print('The results are saved in "results.txt".')


