# -*- coding: utf-8 -*-
# Views in Django are either functions or classes. In our case since we're creating a simple view, we'll create a function.
#install requests to call the API from inside the app.
import requests
# Create your views here.
from django.shortcuts import render
#entries where added to the DB in the from the admin dashboard, we need to query these entries in our view now
from .models import City
from .forms import CityForm


def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d6d7539a50e5354288a49c1c6f9e355b'

    form = CityForm()
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'
    cities = City.objects.all()

    weather_data = []

    for city in cities:
        # try:
            r = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
            weather_info = {
                'city_name' : city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
            weather_data.append(weather_info) #add the data for the current city into our list
        # except KeyError:
        #     pass
        # except EXCEPTION as e:
        #     pass
    context = {'weather_data' : weather_data, 'form' : form}
    ## views will take a request and return a template
    return render(request, 'weather/index.html', context) #returns the index.html template
