# -*- coding: utf-8 -*-
# Views in Django are either functions or classes. In our case since we're creating a simple view, we'll create a function.
#install requests to call the API from inside the app.
import requests
# Create your views here.
from django.shortcuts import render


def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d6d7539a50e5354288a49c1c6f9e355b'
    city='Toronto'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
# Passing the data to index.html template
# weather is a dictionary to hold the data: temp, description, and icon.
    weather_info = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
# to pass weather_info dictionary to index.html template, we'll create a variable called context. This will be a dictionary that allows us to use its values inside of the template.
    context = {'weather_info' : weather_info}
    ## views will take a request and return a template
    return render(request, 'weather/index.html', context) #returns the index.html template
