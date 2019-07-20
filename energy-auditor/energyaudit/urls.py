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
    path('add_bill', views.add_bill, name='add_bill'),
<<<<<<< HEAD
    path(r'^profile/$', views.profile, name='profile'),
    path(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile_with_pk'),
=======
    path('add_addr', views.add_addr, name='add_addr'),
    path('profile', views.profile, name='profile'),
    path('profile', views.profile, name='profile_with_pk'),
>>>>>>> 42fd9a9317716784a418da8a588c7676463c5898
    path('friendsuggestions', views.FriendSuggestions.as_view(), name='friendsuggestions')
]
