import requests

base_currency = input("Enter your base currency code: ").lower()
url = f"http://www.floatrates.com/daily/{base_currency}.json"
response = requests.get(url)
rates = response.json()

cache = {}
# Автоматичне додавання USD та EUR у кеш
for key in ['usd', 'eur']:
    if key in rates:
        cache[key] = rates[key]

while True:
    target_currency = input("Enter currency to convert to (or press Enter to stop): ").lower()
    if target_currency == "":
        break

    amount = float(input("Enter the amount to exchange: "))
    print("Checking the cache...")

    if target_currency in cache:
        print("It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[target_currency] = rates.get(target_currency)

    rate = cache[target_currency]['rate']
    result = round(amount * rate, 2)
    print(f"You received {result} {target_currency.upper()}.")
