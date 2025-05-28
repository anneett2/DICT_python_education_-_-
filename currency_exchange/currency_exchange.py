import requests

currency_code = input("Enter your currency code (e.g. AUD): ").lower()
url = f"http://www.floatrates.com/daily/{currency_code}.json"
response = requests.get(url)

if response.status_code != 200:
    print("Error: Unable to get data. Please check your currency code.")
else:
    try:
        data = response.json()
        usd_rate = None
        eur_rate = None

        if currency_code != 'usd':
            usd_rate = data.get('usd', {}).get('rate')
        if currency_code != 'eur':
            eur_rate = data.get('eur', {}).get('rate')

        if usd_rate:
            print(f"Exchange rate to USD: {usd_rate}")
        else:
            print("Exchange rate to USD is not available (maybe your base currency is USD).")

        if eur_rate:
            print(f"Exchange rate to EUR: {eur_rate}")
        else:
            print("Exchange rate to EUR is not available (maybe your base currency is EUR).")

    except Exception as e:
        print("Error decoding data. Please try again later.")
