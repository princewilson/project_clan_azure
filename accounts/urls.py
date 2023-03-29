from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout_user, name = 'logout'),
    path('callback', views.callback, name = 'callback')
]