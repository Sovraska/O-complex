import requests


async def get_weather(city_name):
    try:
        response = requests.get(
            'https://geocoding-api.open-meteo.com/v1/search'
            '?name={}&count=1'
            .format(city_name)
        )
        data = response.json()
        latitude = data['results'][0]['latitude']
        longitude = data['results'][0]['longitude']
        response = requests.get(
            'https://api.open-meteo.com/v1/forecast'
            '?latitude={0}'
            '&longitude={1}'
            '&hourly=temperature_2m'
            '&format=json'
            '&timeformat=unixtime'
            .format(latitude, longitude)
        )
        data = response.json()
        return (data['hourly']['temperature_2m'], data['hourly']['time'])

    except Exception as ex:
        print("some problem with api", ex)


async def get_ten_city(city_name):
    try:
        url = (
            f'https://geocoding-api.open-meteo.com/v1/search'
            f'?name={city_name}'
            f'&count=5'
            f'&language=en'
            f'&format=json'
        )
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as ex:
        print("some problem with api", ex)
