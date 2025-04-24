import random

correct_answers = 0

for _ in range(5):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])

    while True:
        print(f"{a} {operation} {b}")
        user_input = input()
        try:
            answer = int(user_input)
            if operation == '+':
                correct = a + b
            elif operation == '-':
                correct = a - b
            elif operation == '*':
                correct = a * b
            if answer == correct:
                print("Right!")
                correct_answers += 1
            else:
                print("Wrong!")
            break
        except ValueError:
            print("Incorrect format.")

print(f"Your mark is {correct_answers}/5.")
