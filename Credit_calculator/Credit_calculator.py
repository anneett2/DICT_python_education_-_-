principal = int(input("Enter the loan principal:\n"))

choice = input("""What do you want to calculate?
type "m" - for  number of monthly payments,
type "p" - for the monthly payment:\n""")

if choice == "m":
    monthly_payment = int(input("Enter the monthly payment:\n"))
    months = (principal + monthly_payment - 1) // monthly_payment
    print(f"It will take {months} month{'s' if months > 1 else ''} to repay the loan")
elif choice == "p":
    months = int(input("Enter the number of months:\n"))
    payment = -(-principal // months)
    last_payment = principal - (months -1) * payment
    if payment != last_payment:
        print(f"Your monthly payment = {payment} and the last paymant = {last_payment}")
    else:
        print(f"Your monthly payment = {payment}")
