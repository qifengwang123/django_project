from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says here is the about page!")