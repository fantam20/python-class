from urllib import request
from django.shortcuts import render
from app.views import *

def homepage(request):
    return render(request,"index.html")

def search_bar(request):
    return render(request,"home.index")

def contractpage(request):
    return render(request,"contract.index")