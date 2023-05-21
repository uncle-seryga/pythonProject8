import sqlite3


class DB:
    def __init__(self):
        self.__conn = sqlite3.connect("app_old/static/db.db", check_same_thread=False)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""create table if not exists currency (code,name,rateBuy,rateSell,timeLastUpdate)""")

    def update(self, data):
        for x in data:
            if x["currencyCodeB"] == 980:
                if x['rateBuy'] != 0 and x['rateSell'] != 0:
                    self.__cursor.execute("""update currency set rateBuy=?,rateSell=?,timeLastUpdate=?""",
                                          (x['rateBuy'], x['rateSell'], x['date']))
                else:
                    self.__cursor.execute("""update currency set rateBuy=?,rateSell=?,timeLastUpdate=?""",
                                          (x['rateCross'], x['rateCross'], x['date']))

    def get_currency_name(self,iso_name):
            iso = eval(open('currency/iso4217.json').read())
            for x in iso:
                if int(x["number"]) == iso_name:
                    return x["name"]
                else:
                    return None

    def add_currency(self,data):
            for x in data:
                if x["currencyCodeB"] == 980:
                    if x['rateBuy'] != 0 and x['rateSell'] != 0:
                        self.__cursor.execute(
                            """insert into currency values (rateBuy=?,rateSell=?,timeLastUpdate=?,code=?,name=?)""",
                            (x['rateBuy'], x['rateSell'], x['date'], x['currencyCodeA'],
                             self.get_currency_name(x['currencyCodeA'])))
                    else:
                        self.__cursor.execute(
                            """insert into currency values (rateBuy=?,rateSell=?,timeLastUpdate=?,code=?,name=?)""",
                            (x['rateCross'], x['rateCross'], x['date'], x['currencyCodeA'],
                             self.get_currency_name(x['currencyCodeA'])))

DB().add_currency(eval(open("test.json",'r').read()))