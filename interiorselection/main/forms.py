from .models import *
from django.forms import ModelForm, TextInput, Textarea


class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'description', 'image']
        widgets = {}

class InteriorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.exclude(exist=False)

    class Meta:
        model = Interior
        fields = ['name', 'description', 'room']
        widgets = {}