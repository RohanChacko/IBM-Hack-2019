from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ApplianceForm, MonthlyBillForm, UserLocationForm
from django.db.models import Sum,Avg
from .models import *
from .predictapi import get_disaggregation
import random

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
def dashboard(request):

    context = {}

    if request.META.get('HTTP_REFERER') is not None and 'add_addr' not in request.META.get('HTTP_REFERER'):
        context = dashboard_analytics(request)

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

    # Adding suggestions
    suggestions = get_suggestions(request)
    print (suggestions)
    if suggestions is not None:
        context['suggestions'] = suggestions

    if request.method == 'POST':
        form = MonthlyBillForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()

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
            return redirect('dashboard')

    return render(request, 'home/add_addr.html', context)


def get_suggestions(request):

    SUGGESTION_LIST = {
        'fridge': ["Position your fridge right: Make sure that there is proper \
                    air flow around the refrigerator. Do not place it near windows,\
                    stoves, or ovens. Heat from the sun or cooking appliances can \
                    cause the refrigerator to expend more energy to keep cool.",

                   "Set the correct temperature: The optimum temperature for \
                   refrigerator operation is 5°C, and -18°C for freezer operation.\
                   Stand-alone freezers for long storage can be set at 0 degrees.",

                   "Close fridge door immediately: Avoid opening the door for too long.\
                   Everytime the refrigerator door is opened, cold air escapes and warm\
                   ambient air enters. To compensate for the temperature increase in its\
                   interior, the refrigerator must then use energy to bring the temperature back down."
                   ],

        'ac':    ["Cover the windows in the room: A window letting in the hot sun won't \
                   just heat up your thermostat, it'll heat you up too. During the warmest\
                   part of the day, close your window blinds and keep out the sun. It can \
                   also help insulate your windows, which stops the cold air from escaping.",

                   "Set the temperature high: For air conditioners, the lower the temp, the\
                    more it costs. So, if possible, set the thermostat to the highest temp\
                    that will still keep you feeling cool. Maintaining a temperature that’s\
                    10 to 15 degrees higher than the one you’re used to for 8 hours will save\
                    you a lot of money.",

                   "Make sure the home is well-insulated: One of the things that leads to massive\
                    energy consumption is a poorly-insulated home. Cracks are more common, and seals\
                    are more worn and weathered. To make sure the insulation in your home is good,\
                    have a utility provider or contractor examine your home."
                 ],

        'washing_machine': ["Try to use a big load: A smaller load may use less water, but it will use\
                            the same amount of energy no matter how big the load.",

                            "Run load on the shortest cycle: Run the shortest cycle whenever you can; \
                            they are designed for efficiency.",

                            "Pre-soak stains: Don’t rely on washing machines to take care of stains. \
                            That can often lead to washing things more than once, which uses twice the energy.\
                            Soak your stains in cold water for at least half an hour before washing to save energy."
                           ]
    }

    ## Get avg from friends & see which device is above or below avg
    try:
        friends_monthly_avg = MonthlyBill.objects.exclude(
            owner=request.user).aggregate(avg=Avg('power_consumed'))
    except Exception as e:
        print(e)
        return None


    if friends_monthly_avg is None:
        return None

    total_aggr = friends_monthly_avg['avg']

    disag = DisaggregationResults.objects.filter(
        total_aggregate=12345.0).first()
    if disag is None:
        # Call the model and store the results back
        fridge_estimate = get_disaggregation("fridge", total_aggr)
        ac_estimate = get_disaggregation("air conditioner", total_aggr)
        wm_estimate = get_disaggregation("washing machine", total_aggr)

        disag = DisaggregationResults(
            total_aggregate=total_aggr,
            fridge=fridge_estimate,
            ac=ac_estimate,
            washing_machine=wm_estimate
        )
        disag.save()

    friend_aggr = total_aggr
    friend_obj = disag

    try:
        appliances = Appliance.objects.filter(owner=request.user).values(
            'name').annotate(qty=Sum('quantity')).all()
    except Exception as e:
        print(e)
        return None

    try:
        monthly_bills = MonthlyBill.objects.filter(
            owner=request.user).order_by('-month_year')[:12]
    except Exception as e:
        print(e)
        return None

    total_aggr = monthly_bills.first()
    if total_aggr is None:
        return None

    total_aggr = total_aggr.power_consumed
    # total_aggr.power_consumed
    disag = DisaggregationResults.objects.filter(
        total_aggregate=12346.0).first()
    if disag is None:
        # Call the model and store the results back
        fridge_estimate = get_disaggregation("fridge", total_aggr)
        ac_estimate = get_disaggregation("air conditioner", total_aggr)
        wm_estimate = get_disaggregation("washing machine", total_aggr)

        disag = DisaggregationResults(
            total_aggregate=total_aggr,
            fridge=fridge_estimate,
            ac=ac_estimate,
            washing_machine=wm_estimate
        )
        disag.save()

    suggestions_list = []
    for appl in appliances:
        if appl['name'] == 'fridge' and disag.fridge > friend_obj.fridge:
            suggestions_list.append("Your Fridge is consuming more than your friends' average!")
            suggestions_list.append(random.choice(SUGGESTION_LIST["fridge"]))
        if appl['name'] == 'air conditioner' and disag.ac > friend_obj.ac:
            suggestions_list.append("Your Air Conditioner is consuming more than your friends' average!")
            suggestions_list.append(random.choice(SUGGESTION_LIST["ac"]))
        if appl['name'] == 'washing machine' and disag.washing_machine > friend_obj.washing_machine:
            suggestions_list.append("Your Washing Machine is consuming more than your friends' average!")
            suggestions_list.append(random.choice(SUGGESTION_LIST["washing_machine"]))

    # return {'suggestions':suggestions_list}
    return suggestions_list



def dashboard_analytics(request):

    try:
        monthly_bills = MonthlyBill.objects.filter(
            owner=request.user).order_by('-month_year')[:12]
    except Exception as e:
        print(e)
        return None

    try:
        friends_monthly_bills = MonthlyBill.objects.exclude(
            owner=request.user).order_by('-month_year')[:12]
    except Exception as e:
        print(e)
        return None

    try:
        appliances = Appliance.objects.filter(owner=request.user).values(
            'name').annotate(qty=Sum('quantity')).all()
    except Exception as e:
        print(e)
        return None

    total_aggr = monthly_bills.first()
    if total_aggr is None:
        return None

    total_aggr = total_aggr.power_consumed
    # total_aggr.power_consumed
    disag = DisaggregationResults.objects.filter(
        total_aggregate=12345.0).first()
    if disag is None:
        # Call the model and store the results back
        fridge_estimate = get_disaggregation("fridge", total_aggr)
        ac_estimate = get_disaggregation("air conditioner", total_aggr)
        wm_estimate = get_disaggregation("washing machine", total_aggr)

        disag = DisaggregationResults(
            total_aggregate=total_aggr,
            fridge=fridge_estimate,
            ac=ac_estimate,
            washing_machine=wm_estimate
        )
        disag.save()

    appl_dict = {}
    others = total_aggr
    for appl in appliances:
        if appl['name'] == 'fridge':
            appl_dict[appl['name']] = disag.fridge
            others -= disag.fridge
        if appl['name'] == 'air conditioner':
            appl_dict[appl['name']] = disag.ac
            others -= disag.ac
        if appl['name'] == 'washing machine':
            appl_dict[appl['name']] = disag.washing_machine
            others -= disag.washing_machine

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
