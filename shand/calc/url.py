from  django.urls import path, include
from django.contrib import admin 

from . import views

urlpatterns = [ 
    path('', include("calc.urls")),
    path('',views.home, name= "home"),
    ]