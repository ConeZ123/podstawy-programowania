from SensorDataset import SensorDataset

class SensorStats:
    def __init__(self, data):
        self._data = data.get_dataset()
        self._url = data.get_url()
        self._sensor_type = data.get_sensor_type()
