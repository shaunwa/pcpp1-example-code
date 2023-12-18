import requests

# response = requests.get('https://restcountries.com/v3.1/name/usa')

# country_info = response.json()[0]

# print(f'The capital of the country is: {country_info["capital"]}')
# print(f'The population of the country is: {country_info["population"]}')

response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=4990729&appid=08b7e56615d0752156e6ecafb523fd7d')

weather_data = response.json()

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

for data_point in weather_data['list']:
    print(f'{data_point["dt_txt"]}: {kelvin_to_celsius(float(data_point["main"]["temp"]))}')

# response = requests.get('http://localhost:8000')
# for thing in response:
#     print(thing)