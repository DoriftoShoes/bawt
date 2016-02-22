import requests
import time

from bawt.bawt import Bawt
from bawt import log as logging

LOG = logging.get_logger(__name__)

HTTP_OK_CODES = [200, 201, 202]
SLEEP = 2


class Weather(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.location = self.weather.get('location', None)
        LOG.info("Location is set to: %s" % self.location)
        self.appid = self.weather.get('appid', None)
        LOG.info("APPID: %s" % self.appid)
        if self.appid == None:
            LOG.critical("No location set for weather info.")

    def get_data(self):
        data = {
                'q': self.location,
                'APPID': self.appid
               }

        r = requests.get(self.weather.get('url', None), params=data)

        try:
            response = r.json()
        except:
            LOG.critical('Response to weather API was not json')
            return False

        return_code = response.get('cod', 0)
        if return_code == 401:
            LOG.warn("Received 401.  Sleeping for %i seconds before retry" % SLEEP)
            time.sleep(SLEEP)
            self.get_data()
            return
        elif return_code not in HTTP_OK_CODES:
            LOG.critical('Response from weather API was invalid: %s' % r.text)
            return False

        return response

    def get_weather(self):
        weather_data = self.get_data()
        if not weather_data:
            LOG.critical("Failed to retrieve weather data")
            return False

        print weather_data
        return weather_data.get('weather', None)

    def is_raining(self):
        weather = self.get_weather()
        if not weather:
            LOG.critical("Weather data is invalid")
            return False

        if weather.get('id', None) == '500':
            return True
        else:
            return False
