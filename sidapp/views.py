from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Yo, its Siddhartha Arora")

# Create your views here.
