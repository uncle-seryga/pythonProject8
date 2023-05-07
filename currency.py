import requests


def get_currency():
    data = requests.get("https://api.monobank.ua/bank/currency").text
    data = eval(data)
    if data.get("'errorDescription'") == 'Too many requests':
        return None
    else:

        return data


print(get_currency())
