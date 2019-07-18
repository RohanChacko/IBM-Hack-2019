from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ApplianceForm
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
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'register_active': 'active',
    }
    return render(request, 'home/register.html', context)

def login_user(request):

    username = password = ''
    context = {
    'login_active': 'active',
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'home/login.html', context)
        # return render_to_response('login.html', context_instance=RequestContext(request))

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):

    context = {
        'dashboard_active': 'active',
    }

    return render(request, 'account/dashboard.html', context)

@login_required
def leaderboard(request):

    context = {
        'leaderboard_active': 'active',
    }
    return render(request, 'account/leaderboard.html', context)

@login_required
def profile(request):

    context = {
        'profile_active': 'active',
    }

    return render(request, 'account/profile.html', context)

@login_required
def query(request):
    context = {
        'profile_active': 'active',
        'form': ApplianceForm(),
    }

    if request.method == 'POST':

        form = ApplianceForm(request.POST)
        print(request.POST)
        print(form)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('dashboard')
            
    return render(request, 'account/query.html', context)


class FriendSuggestions(TemplateView):
    template_name = "users/friend_suggestions.html"

    def get(self, request):

        users = User.objects.all()

        context = {
            'users' : users,
        }

        return render(request, self.template_name, context)
