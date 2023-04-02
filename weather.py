import requests
import datetime


class Weather:
    def __init__(self, city_name):
        __API_key = "e90fab7014064d2c88795d9fd95afa6f"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={__API_key}&units=metric"
        self.data = eval(requests.get(url).text)
        print(self.data)
        self.temp = self.data["main"]["temp"]
        self.sky = self.data["weather"][0]['main']
        self.time = str(datetime.datetime.now())[:-7]
        self.icon = self.data["weather"][0]['icon']
        self.lat = self.data['coord']['lat']
        self.lon = self.data['coord']['lon']
        self.city = city_name


Weather("Kyiv")
