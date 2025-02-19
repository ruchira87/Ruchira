import requests

#Test
def get_weather(city):
    api_key = "e1da05625b54c36d6b4c8a4b61cc568b"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q':city,'appid':api_key,'units':'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code==200:
        data = response.json()
        print(f"city:{data['name']}")

        print(f"temperature:{data['main']['temp']}C")

        print(f"Weather:{data['weather'][0]['description']}")

    else:

        print("city is not found")

def get_wether_forcast(city):
    api_key = "e1da05625b54c36d6b4c8a4b61cc568b"
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {'q':city,'appid':api_key,'units':'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code==200:
        data = response.json()
        print("Weather forecast for " + data['city']['name'])
        print(f"{data['cnt']}forecast retrieve")

        for forecast in data ['list'][:4]:
            Temperature = forecast ['main']['temp']
            description = forecast['weather'][0]['description']
            print (f"Temp:{Temperature}, Desc:{description}" )

    else:
        print("city is not found")   
    
    
    
city = input ("enter a city ")
get_weather(city) 
get_wether_forcast(city)







