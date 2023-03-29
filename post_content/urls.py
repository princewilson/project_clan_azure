from django.urls import path
from . import views

urlpatterns = [
    path('make_a_post/', views.make_a_post, name = 'make_a_post')
]