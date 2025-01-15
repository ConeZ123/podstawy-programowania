import requests
import json

class SensorDataset():
    def __init__(self, url, sensor_type):
        self._url = url
        self._sensor_type = sensor_type
        self._data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self._url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Błąd pobierania danych")
        
    def get_url(self, url):
        return self._url

    def get_sensor_type(self, sensor_type):
        return self._sensor_type

    def get_dataset(self):
        return self._data.get(self._sensor_type)