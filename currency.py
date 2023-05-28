import requests


def download_currency():
    data = requests.get("https://api.monobank.ua/bank/currency").text
    data = eval(data)
    if type(data) == list:
        save_currency_json(data)
        return data
    else:
        return None


def save_currency_json(data):
    with open('currency/data.json', 'w') as f:
        f.write(str(data))


def set_currency():
    exceptions = []
    results = {}
    with open('currency/countries.json','r') as counties:
        counties = eval(counties.read())
    with open('currency/data.json', 'r') as cur:
        cur_data = eval(cur.read())
        with open('currency/iso4217.json', 'r') as iso:
            iso_data = eval(iso.read())
            for x in cur_data:
                if x['rateBuy'] == 0 and x['currencyCodeB'] != 840:
                    for y in iso_data:
                        if y['number'] == str(x['currencyCodeA']):
                            for z in counties:
                                try:
                                    if y["code"] in z['currencies'] and y['code'] not in exceptions:
                                        results.update({y["code"]: [x['rateCross'], y['name'],z['cca2']]})
                                        exceptions.append(y['code'])
                                        break
                                except KeyError:
                                        results.update({y["code"]: [x['rateCross'], y['name'], z['cca2']]})
                                        break
                elif x['currencyCodeB'] != 840:
                    for y in iso_data:
                        if y['number'] == str(x['currencyCodeA']):
                            for z in counties:
                                if y["code"] in z['currencies'] and y['code'] not in exceptions:
                                    results.update({y["code"]: [x['rateBuy'], y['name'] ,z['cca2']]})
                                    exceptions.append(y['code'])
                                    break
    return results

# print(set_currency())
