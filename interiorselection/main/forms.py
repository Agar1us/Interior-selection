from .models import *
from django import forms

class RoomsForm(forms.Form):

    name = forms.CharField(max_length=40, label='Название комнаты')
    image = forms.ImageField(label='Фотография комнаты', required=False)

class InteriorForm(forms.Form):

    name = forms.CharField(max_length=50, label='Предмет')
    room = forms.ModelChoiceField(queryset=Rooms.objects.all(), required=False)