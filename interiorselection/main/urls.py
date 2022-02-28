from django.urls import path
from . import views

urlpatterns = [
    path('home', views.mainpg, name='home'),
    path('contacts', views.about, name='contacts'),
    path('cabinets', views.cabinets, name='cabinets'),
    path('stock', views.stock, name='stock'),
    path('faqs', views.faqs, name='faqs'),
]