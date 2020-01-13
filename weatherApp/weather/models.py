# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#to hard code the city and pull from the database, then  show the cities that are in our database > we'll create a table in our database to hold the cities that we want to know the weather for. We'll create a model for this.

class City(models.Model):
# This will create a table in our database that will have a column called name (a string)
    name = models.CharField(max_length=25)

    def _str_(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys in the admin dashboard
        verbose_name_plural = 'cities'
