from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('register_details', views.register_details, name='register_details'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('profile', views.profile, name='profile'),
    path('profile', views.profile, name='profile_with_pk'),
    path('friendsuggestions', views.FriendSuggestions.as_view(), name='friendsuggestions')
]
