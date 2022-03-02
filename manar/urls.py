from unicodedata import name
from django.urls import path, include
from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('about/' ,views.about,name='RODIOLOGY' ), 
    path('operation/'  ,views.operation ,name='operation'),
    path('dialaysis/',views.dialaysis ,name='dialaysis'),
    path('medical/',views.medical ,name='medical'),
    path('hotel/',views.hotel,name='hotelmagement')
    
]