import requests

API_KEY = "#####################"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
LANG = "pt_br"

city = input("Digite o nome da cidade: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&lang={LANG}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 272.15, 2)
    print("Condição Meteorológica:", weather)
    print("Temperatura:", temperature, "ºC")
else:
    print("Ocorreu uma falha.")