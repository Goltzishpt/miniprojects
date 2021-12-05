# Code
# Это самая первая программа написанная мною по видео-уроку от Хауди-Хо

from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('ba4d6110d51e45fa5968d89d8fb3fa55')
mgr = owm.weather_manager()

place = input("Где нужно узнать погоду?: ")

observation = mgr.weather_at_place(place)
w = observation.weather


print("В городе " + place.capitalize() + " сейчас " + str(w.detailed_status))
