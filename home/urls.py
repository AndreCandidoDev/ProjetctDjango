from django.contrib import admin
from django.urls import path
from .views import home
from .views import Logout
from .views import HomePageView
from .views import MyView
from .views import polices
from .views import services_term
from .views import exclusion
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('logout/', Logout, name='logout'),
    path('polices/', polices, name='polices'),
    path('services_terms/', services_term, name='services_term'),
    path('exclusion/', exclusion, name='exclusion'),
    path('home2/', TemplateView.as_view(template_name='home2.html')),  # direciona para uma view generica
    path('home3/', HomePageView.as_view(template_name='home3.html')),
    path('view/', MyView.as_view())
]