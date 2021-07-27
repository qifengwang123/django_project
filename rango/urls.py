from django.urls import path
from rango import about, views

app_name = 'rango'

urlpatterns = [
path('', views.index, name='index'),
path('', views.about, name='index'),
]