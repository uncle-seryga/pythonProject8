import requests
import codecs


def download_currency():
    data = requests.get("https://api.monobank.ua/bank/currency").text
    data = eval(data)
    if type(data) == list:
        save_currency_json(data)
        return data
    else:
        return None


def save_currency_json(data):
    with codecs.open('currency/data.json', 'w', 'utf-8') as f:
        f.write(str(data))


def set_currency():
    exceptions = []
    results = {}
    with open('currency/countries.json', 'r') as counties:
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
                                        results.update({y["code"]: [x['rateCross'], y['name'], z['cca2']]})
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
                                    results.update({y["code"]: [x['rateBuy'], y['name'], z['cca2']]})
                                    exceptions.append(y['code'])
                                    break
    return results


def convert(cur1, cur2, amount):
    iso = eval(open('currency/iso4217.json', 'r').read())
    for x in iso:
        if x["code"] == cur1:
            cur1_code = int(x["number"])
    else:
        cur1_code = 980
    for x in iso:
        if x["code"] == cur2:
            cur2_code = int(x["number"])
    else:
        cur2_code = 980
    data = eval(open('currency/data.json', 'r').read())
    for x in data:
        if x["currencyCodeA"] == cur1_code:
            if x['rateBuy'] == 0:
                cur1_price = x['rateCross']
            else:
                cur1_price = x['rateBuy']
    else:
        cur1_price = 1
    for x in data:
        if x["currencyCodeA"] == cur2_code:
            if x['rateBuy'] == 0:
                cur2_price = x['rateCross']
            else:
                cur2_price = x['rateBuy']
    else:
        cur2_price = 1
    return (cur2_price / cur1_price * amount)
