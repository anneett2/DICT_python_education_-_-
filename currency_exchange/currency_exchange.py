mycoins = float(input("Enter the number of mycoins: "))

rates = {
    "ARS": 0.82,
    "HNL": 0.17,
    "AUD": 1.9622,
    "MAD": 0.208
}

for currency, rate in rates.items():
    result = round(mycoins * rate, 2)
    print(f"I will get {result} {currency} from the sale of {mycoins} mycoins.")
