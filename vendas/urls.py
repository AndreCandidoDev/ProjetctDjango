from django.contrib import admin
from django.urls import path
from .views import DashboardView


# app_name = 'clientes'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard')
    ]
