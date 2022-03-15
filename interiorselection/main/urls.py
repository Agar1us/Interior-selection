from django.urls import path
from . import views

urlpatterns = [
    path('home', views.mainpg, name='home'),
    path('contacts', views.about, name='contacts'),
    path('cabinets', views.cabinets, name='cabinets'),
    path('stock', views.ListObjects.as_view(), name='stock'),
    path('faqs', views.faqs, name='faqs'),
    path('displacement', views.DisplacementView.as_view(), name='displacement'),
    path('create_room', views.CreateRoomView.as_view(), name='create_room'),
]
