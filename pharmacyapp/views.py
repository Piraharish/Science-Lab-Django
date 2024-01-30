from django.shortcuts import render
from django.shortcuts import *

def index(request):
    return render (request,'index.html')

