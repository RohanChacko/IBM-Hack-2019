from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Sample
def home(request):
    name = "Blueticks"
    context = {
        "name": name,
    }
    return render(request, "hello_world.html", context)
