from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpg, name='home'),
    path('home', views.mainpg, name='home'),
    path('contacts', views.about, name='contacts'),
    path('stock', views.ListInterior.as_view(), name='stock'),
    path('stock/<int:id>/', views.DetailInterior.as_view(), name='stock_detail'),
    path('stock/<int:id>/update', views.UpdateInterior.as_view(), name='stock_update'),
    path('stock/<int:id>/delete', views.DeleteInterior.as_view(), name='stock_delete'),
    path('faqs', views.faqs, name='faqs'),
    path('displacement', views.DisplacementView.as_view(), name='displacement'),
    path('cabinets', views.CabinetsView.as_view(), name='cabinets'),
    path('create_room', views.CreateRoomView.as_view(), name='create_room'),
    path('room/<int:id>/', views.RoomView.as_view(), name='room'),
    path('room/<int:id>/update', views.UpdateRoomView.as_view(), name='update_room'),
    path('room/<int:id>/delete', views.DeleteRoomView.as_view(), name='delete_room'),
]
