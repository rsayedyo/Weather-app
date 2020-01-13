# -*- coding: utf-8 -*-
# Views in Django are either functions or classes. In our case since we're creating a simple view, we'll create a function.
#install requests to call the API from inside the app.
import requests
# Create your views here.
from django.shortcuts import render
#entries where added to the DB in the from the admin dashboard, we need to query these entries in our view now
from .models import City
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d6d7539a50e5354288a49c1c6f9e355b'
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        try:
            city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

            weather_info = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }

            weather_data.append(weather-info) #add the data for the current city into our list
        except KeyError:
            pass
        except EXCEPTION as e:
            pass
    context = {'weather_data' : weather_data}
    ## views will take a request and return a template
    return render(request, 'weather/index.html', context) #returns the index.html template
