from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('query', views.query, name='query'),
    path('add_bill', views.add_bill, name='add_bill'),
    path('profile', views.profile, name='profile'),
    path('profile', views.profile, name='profile_with_pk'),
    path('friendsuggestions', views.FriendSuggestions.as_view(), name='friendsuggestions')
]
