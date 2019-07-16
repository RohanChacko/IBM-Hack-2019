from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

from django.contrib.auth.models import User


# Create your views here.

def index(request):

    context = {
        'home_active': 'active',
    }

    return render(request, 'home/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'register_active': 'active',
    }
    return render(request, 'home/register.html', context)

def login(request):

    context = {
        'login_active': 'active',
    }

    return render(request, 'home/login.html', context)

def dashboard(request):

    context = {
        'dashboard_active': 'active',
    }

    return render(request, 'account/dashboard.html', context)

def leaderboard(request):

    context = {
        'leaderboard_active': 'active',
    }
    return render(request, 'account/leaderboard.html', context)

class FriendSuggestions(Template):
    template_name = "users/friend_suggestions.html"

    def get(self, request):

        users = User.objects.all()

        context = {
            'users' : users, 
        }

        return render(request, self.template_name, context)


    return render(request, 'account/leaderboard.html', context)

def profile(request):

    context = {
        'profile_active': 'active',
    }

    return render(request, 'account/profile.html', context)
