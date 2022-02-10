# Program which takes in live currency rates and converts them to User Specified Currency
# Also A Program for Bitcoin Exchange Rates in USD
# Updates Value for every 5 Seconds

import requests


def CurrencyExchange():
    # Input Values
    currency1 = input("Enter the Currency code to be converted: ").upper()
    amt1 = float(input("Enter the Amount: "))
    currency2 = input("Enter the Currency code to convert to: ").upper()

    currencyURl = str(
        f"https://free.currconv.com/api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey=c941e34a027dbeb2665b")

    url_response = requests.get(currencyURl)
    # print(url_response)

    data_JSON = url_response.json()
    data_JSON = float(data_JSON[f'{currency1}_{currency2}'])
    amt2 = round(data_JSON * amt1, 2)
    print(f"Converted Rate {currency1}--{currency2} : ", amt2)


def BitcoinExchange():
    import requests
    import time

    bitcoin_URL = "https://blockchain.info/ticker"
    response_url = requests.get(bitcoin_URL)

    while True:
        usd_rate = response_url.json()['USD']['last']
        print(f"Rate at {time.strftime('%d-%b-%y %H:%M:%S')} -- {usd_rate}$")
        time.sleep(5)
