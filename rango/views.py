
#chapter3
# from django.http import HttpResponse
#def index(request):
    #return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")
#def about(request):
 #   return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Refer to the TwD book for more information on how this updated view works.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'rango/about.html')

