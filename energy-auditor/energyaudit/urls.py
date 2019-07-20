from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('register_details', views.register_details, name='register_details'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard_analytics', views.dashboard_analytics, name='dashboard_analytics'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('add_bill', views.add_bill, name='add_bill'),
    path('add_appl', views.add_appl, name='add_appl'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:pk>', views.profile, name='profile_with_pk'),
    path('add_addr', views.add_addr, name='add_addr'),
    path('friendsuggestions', views.FriendSuggestions.as_view(), name='friendsuggestions')
]
