from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("",homepage,name="home"),
    path("/contract",contractpage,name="contract"),
]