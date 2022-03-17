from django.urls import path
from . import views

urlpatterns = [
    path('home', views.mainpg, name='home'),
    path('contacts', views.about, name='contacts'),
    path('cabinets', views.cabinets, name='cabinets'),
    path('stock', views.ListInterior.as_view(), name='stock'),
    path('stock/<int::id>', views.DetailInterior.as_view(), name='stock_detail'),
    path('stock/<int::id>/delete', views.DeleteInterior.as_view(), name='stock_delete'),
    path('faqs', views.faqs, name='faqs'),
    path('displacement', views.DisplacementView.as_view(), name='displacement'),
    path('create_room', views.CreateRoomView.as_view(), name='create_room'),
]
