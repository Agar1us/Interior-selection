from .models import *
from django import forms

class RoomForm(forms.Form):

    name = forms.CharField(max_length=50, label='Предмет')
    description = forms.CharField(label='Описание предмета', required=False)
    image = forms.ImageField(label='Фотография комнаты', required=False)

class InteriorForm(forms.Form):

    name = forms.CharField(max_length=50, label='Предмет')
    description = forms.CharField(label='Описание предмета', required=False)
    room = forms.ModelChoiceField(label='Комната', queryset=Room.objects.exclude(exist=False))