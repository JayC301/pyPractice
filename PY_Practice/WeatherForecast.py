import os
import requests

weather_forecast_api = "4750acfc42377fc5ec19b4b67bea1f80"
location = input("Enter the location that you would like to forecast the weather: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location + "&appid=" + weather_forecast_api
forecast_api_link = "https://api.openweathermap.org/data/2.5/forecast?q=" + location + "&appid=" + weather_forecast_api
api_link = requests.get(forecast_api_link)
api_data = api_link.json()
# print(api_data)


#5day/3hour weather forecast code
if api_data['cod'] == '404':
    print("Invalid city entered:{}, please check your city name".format(location))
else:
    for i in range(5):
        temp_city = api_data["list"][i]["main"]["temp"] - 273.15
        weather_desc = api_data["list"][i]['weather'][0]['description']
        hmdt = api_data["list"][i]['main']['humidity']
        wind_speed = api_data["list"][i]['wind']['speed']
        time = api_data["list"][i]["dt_txt"]

        print("---------------------------------------------------------------------------------------")
        print("Weather stats for {} || {}".format(location, time))
        print("---------------------------------------------------------------------------------------")

        print("City temperature       : {:.2f} deg C".format(temp_city))
        print("Weather description    : {}".format(weather_desc))
        print("Humidity               : {}%".format(hmdt))
        print("Wind speed             : {}kmph".format(wind_speed))

#Current Weather Forecast Code
# if api_data['cod'] == '404':
#     print("Invalid city entered:{}, please check your city name".format(location))
# else:
#     temp_city = api_data["main"]["temp"] - 273.15
#     weather_desc = api_data['weather'][0]['description']
#     hmdt = api_data['main']['humidity']
#     wind_speed = api_data['wind']['speed']

#     print("---------------------------------------------------------------------------------------")
#     print("Weather stats for {}".format(location))
#     print("---------------------------------------------------------------------------------------")

#     print("Current city temperature       : {:.2f} deg C".format(temp_city))
#     print("Current weather description    : {}".format(weather_desc))
#     print("Current humidity               : {}%".format(hmdt))
#     print("Current wind speed             : {}kmph".format(wind_speed))