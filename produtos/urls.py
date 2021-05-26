from django.contrib import admin
from django.urls import path
from .views import *

# app_name = 'clientes'

urlpatterns = [
        path('produto_list', ProdutoList.as_view(), name='produto_list'),
        path('produto_detail/<int:pk>/', ProdutoDetail.as_view(), name='produto_detail'),
        path('produto_update/<int:pk>/', ProdutoUpdate.as_view(), name='produto_update'),
        path('produto_delete/<int:pk>/', ProdutoDelete.as_view(), name='produto_delete'),
        path('produto_create/', ProdutoCreate.as_view(), name='produto_create'),
    ]