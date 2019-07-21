from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ApplianceForm, MonthlyBillForm, UserLocationForm
from django.db.models import Sum
from .models import *
from .predictapi import get_disaggregation

# Create your views here.


def index(request):

    context = {
        'home_active': 'active',
    }
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'home/index.html', context)


def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('register_details')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'register_active': 'active',
    }
    return render(request, 'home/register.html', context)


@login_required
def register_details(request):
    context = {
        'register_active': 'active',
        'form_fridge': ApplianceForm(prefix='fridge'),
        'form_ac': ApplianceForm(prefix='ac'),
        'form_washingmachine': ApplianceForm(prefix='washingmachine'),
    }

    if request.method == 'POST':

        form_fridge = ApplianceForm(request.POST, prefix='fridge')
        form_ac = ApplianceForm(request.POST, prefix='ac')
        form_washingmachine = ApplianceForm(
            request.POST, prefix='washingmachine')

        if form_fridge.is_valid():
            post = form_fridge.save(commit=False)
            post.owner = request.user
            post.save()

        if form_ac.is_valid():
            post = form_ac.save(commit=False)
            post.owner = request.user
            post.save()

        if form_washingmachine.is_valid():
            post = form_washingmachine.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('add_addr')

    else:
        return render(request, 'home/questionnaire.html', context)


def login_user(request):

    username = password = ''

    context = {
        'login_active': 'active',
    }

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'home/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def dashboard(request, new=None):

    context = {}

    if new is None:
        context = dashboard_analytics(request)
        if context is None:
            context = {}
    context['dashboard_active'] = 'active'

    return render(request, 'account/dashboard.html', context)


@login_required
def leaderboard(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    users = User.objects.exclude(id=request.user.id)
    location = UserLocation.objects.exclude(
        owner=request.user).values('city', 'state').all()

    context = {
        'leaderboard_active': 'active',
        'users': users,
        'location': location,
    }

    return render(request, 'account/leaderboard.html', context)


@login_required
def profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
        # print(user.username)
    else:
        user = request.user

    location = UserLocation.objects.filter(owner=request.user).values(
        'building', 'street', 'city', 'state')

    context = {
        'profile_active': 'active',
        'user': user,
        'location': location,
    }

    return render(request, 'account/profile.html', context)


@login_required
def add_bill(request):
    context = {
        'monthlybill_active': 'active',
        'form': MonthlyBillForm(),
    }

    if request.method == 'POST':
        form = MonthlyBillForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('add_bill')

    return render(request, 'account/add_bill.html', context)


@login_required
def add_appl(request):
    context = {
        'monthlybill_active': 'active',
        'form': ApplianceForm(),
    }

    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('dashboard')

    return render(request, 'account/add_appl.html', context)


@login_required
def add_addr(request):
    context = {
        'register_active': 'active',
        'form': UserLocationForm(),
    }

    if request.method == 'POST':
        form = UserLocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('dashboard', True)

    return render(request, 'home/add_addr.html', context)


def dashboard_analytics(request):

    try:
        monthly_bills = MonthlyBill.objects.filter(
            owner=request.user).order_by('-month_year')[:12]
    except Exception as e:
        print(e)
        return redirect('dashboard', new=True)

    try:
        friends_monthly_bills = MonthlyBill.objects.exclude(
            owner=request.user).order_by('-month_year')[:12]
    except Exception as e:
        print(e)
        return redirect('dashboard')

    try:
        appliances = Appliance.objects.filter(owner=request.user).values(
            'name').annotate(qty=Sum('quantity')).all()
    except Exception as e:
        print(e)
        return redirect('dashboard')

    total_aggr = monthly_bills.first()
    if total_aggr is None:
        return None

    total_aggr = total_aggr.power_consumed
    # total_aggr.power_consumed
    disag = DisaggregationResults.objects.filter(
        total_aggregate=total_aggr).first()
    if disag is None:
        # Call the model and store the results back
        fridge_estimate = get_disaggregation("fridge",total_aggr)
        ac_estimate = get_disaggregation("air conditioner",total_aggr)
        wm_estimate = get_disaggregation("washing machine",total_aggr)

        disag = DisaggregationResults(total_aggregate=total_aggr, fridge=fridge_estimate, ac=ac_estimate, washing_machine=wm_estimate)
        disag.save()

    appl_dict = {}
    others = total_aggr
    for appl in appliances:
        if appl['name'] == 'fridge':
            appl_dict[appl['name']] = disag.fridge
            # appl_dict[appl['name']] = appl['qty']*disag.fridge
            others -= disag.fridge
        if appl['name'] == 'air conditioner':
            appl_dict[appl['name']] = disag.ac
            others -= disag.ac
            # appl_dict[appl['name']] = appl['qty']*disag.ac
        if appl['name'] == 'washing machine':
            appl_dict[appl['name']] = disag.washing_machine
            others -= disag.washing_machine
            # appl_dict[appl['name']] = appl['qty']*disag.washing_machine

    appl_dict["others"] = others

    context = {
        'bills': monthly_bills,
        'friends_bills': friends_monthly_bills,
        'appliances': appl_dict,
    }

    return context


# class FriendSuggestions(TemplateView):
#     template_name = "users/friend_suggestions.html"
#
#     def get(self, request):
#
#         users = User.objects.exclude(id=request.user.id)
#
#         context = {
#             'users' : users,
#         }
#
#         return render(request, self.template_name, context)
