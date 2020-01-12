# -*- coding: utf-8 -*-
# Views in Django are either functions or classes. In our case since we're creating a simple view, we'll create a function.

# Create your views here.
from django.shortcuts import render

def index(request):
    ## views will take a request and return a template
    return render(request, 'weather/index.html') #returns the index.html template
