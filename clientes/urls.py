from django.contrib import admin
from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
# =========== CBV ========================
from .views import PersonList
from .views import PersonDetail
from .views import PersonCreate
from .views import PersonUpdate
from .views import PersonDelete
# ================== Bulk ==================================
from .views import ProdutoBulk

# app_name = 'clientes'

urlpatterns = [
    # FBV urls
    path('list/', persons_list, name='persons_list'),
    path('new/', persons_new, name='persons_new'),
    path('update/<int:id>/', persons_update, name='persons_update'),
    path('delete/<int:id>/', persons_delete, name='persons_delete'),

    # CBV urls
    path('person_list', PersonList.as_view(), name='person_list_cbv'),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name='person_detail_cbv'),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name='person_update_cbv'),
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name='person_delete_cbv'),
    path('person_create', PersonCreate.as_view(), name='person_create_cbv'),

    # Bulk urls
    path('person_bulk/', ProdutoBulk.as_view(), name='person_bulk'),
]