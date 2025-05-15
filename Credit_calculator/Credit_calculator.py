import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

# Перевірка на правильність параметрів
args_list = [args.payment, args.principal, args.periods, args.interest]
if not args.type or args.interest is None or any(x is not None and x < 0 for x in args_list):
    print("Incorrect parameters")
    sys.exit()

i = args.interest / (12 * 100)

if args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
        sys.exit()
    total = 0
    for m in range(1, args.periods + 1):
        d = args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods)
        d = math.ceil(d)
        total += d
        print(f"Month {m}: payment is {d}")
    print(f"Overpayment = {int(total - args.principal)}")

elif args.type == "annuity":
    if args.principal and args.periods:
        A = math.ceil(args.principal * i * (1 + i)**args.periods / ((1 + i)**args.periods - 1))
        print(f"Your annuity payment = {A}!")
        print(f"Overpayment = {int(A * args.periods - args.principal)}")
    elif args.payment and args.periods:
        P = args.payment / ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1))
        print(f"Your loan principal = {int(P)}!")
        print(f"Overpayment = {int(args.payment * args.periods - P)}")
    elif args.principal and args.payment:
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        years, months = divmod(n, 12)
        y_str = f"{years} year{'s' if years != 1 else ''}" if years else ""
        m_str = f"{months} month{'s' if months != 1 else ''}" if months else ""
        and_str = " and " if years and months else ""
        print(f"It will take {y_str}{and_str}{m_str} to repay this loan!")
        print(f"Overpayment = {int(args.payment * n - args.principal)}")
    else:
        print("Incorrect parameters")
