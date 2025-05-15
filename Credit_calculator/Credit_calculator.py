import math
from random import choice

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p for loan principal:""")
choice = input("> ")

if choice == "n":
    P = float(input("Enter the loan principal:\n"))
    A = float(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    n = math.ceil(math.log(A / (A - i * P), 1 + i))
    years, months = divmod(n, 12)
    y_str = f"{years} year{'s' if years != 1 else ''}" if years else ""
    m_str = f"{months} month{'s' if months != 1 else ''}" if months else ""
    and_str = " and " if years and months else ""
    print(f"It will take {y_str}{and_str}{m_str} to repay this loan!")
    print(f"Overpayment = {int(A * n - P)}")

elif choice == "a":
    P = float(input("Enter the loan principal:\n"))
    n = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    A = P * (i * (1 + i)**n) / ((1 + i)**n - 1)
    print(f"Your annuity payment = {math.ceil(A)}!")
    print(f"Overpayment = {math.ceil(A) * n - int(P)}")

elif choice == "p":
    A = float(input("Enter the annuity payment:\n"))
    n = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    P = A / ((i * (1 + i)**n) / ((1 + i)**n - 1))
    print(f"Your loan principal = {int(P)}!")
    print(f"Overpayment = {int(A * n - P)}")