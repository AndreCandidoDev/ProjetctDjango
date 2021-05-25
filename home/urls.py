from django.contrib import admin
from django.urls import path
from .views import home
from .views import Logout
from .views import HomePageView
from .views import MyView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('logout/', Logout, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html')),  # direciona para uma view generica
    path('home3/', HomePageView.as_view(template_name='home3.html')),
    path('view/', MyView.as_view())
]