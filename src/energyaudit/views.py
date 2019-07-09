from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Sample
def home(request):
    return HttpResponse("Hello Blue Ticks")
