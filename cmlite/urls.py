from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_search, name='contact_search'),
    path('add_contacts/', views.add_contacts, name='add_contacts'),
    path('quick_search/', views.quick_search, name='quick_search'),
]
