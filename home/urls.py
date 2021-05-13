from django.contrib import admin
from django.urls import path
from .views import home
from .views import Logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', Logout, name='logout')
]