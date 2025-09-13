import requests
def weather_query(city):
    print(city)
    API_KEY = "e93a06ac15c04661aee1ba097d3de3df"

    BASE_URL = "https://r96yvxvxpj.re.qweatherapi.com"
    urls_position = f"{BASE_URL}/geo/v2/city/lookup"
    params = {
        "location": city,
        "key": API_KEY
    }

    response = requests.get(urls_position, params=params, timeout=10)
    data = response.json()
    # print(data)
    id = data['location'][0]['id']

    url_weather = f"{BASE_URL}/v7/weather/now"
    params = {
        "location": id,
        "key": API_KEY
    }
    response = requests.get(url_weather, params=params, timeout=10)
    data = response.json()
    # print(data['now']['temp'],data['now']['text'],data['now']['windDir'],data['now']['windScale'])
    return {'temp':data['now']['temp'],'text':data['now']['text'],'windDir':data['now']['windDir'],'windSpeed':data['now']['windSpeed']}

if __name__ == '__main__':
    print(weather_query("121.47,31.23"))
