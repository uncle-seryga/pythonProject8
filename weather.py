import requests
import datetime


class Weather:
    def __init__(self, city_name:str):

        __API_key = "e90fab7014064d2c88795d9fd95afa6f"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={__API_key}&units=metric"
        self.data = eval(requests.get(url).text)
        print(self.data)
        self.temp = self.data["main"]["temp"] if city_name is not None else 0
        self.sky = self.data["weather"][0]['main'] if city_name is not None else "Bebra"
        self.time = str(datetime.datetime.now())[:-7]
        self.icon = self.data["weather"][0]['icon']
        self.lat = self.data['coord']['lat'] if city_name is not None else 0
        self.lon = self.data['coord']['lon'] if city_name is not None else 0
        self.city: str = city_name.title() if city_name is not None else None
