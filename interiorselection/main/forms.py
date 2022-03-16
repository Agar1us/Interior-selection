from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileInput, CheckboxInput

class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'description', 'image']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control py-1',
            }),
            'description': Textarea(attrs={
                'class': 'form-control py-1',
                'cols': '40',
                'rows': '7'
            }),
            'image': CheckboxInput(attrs={
                'class': 'form-control py-1',
            }),
        }

class InteriorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.exclude(exist=False)

    class Meta:
        model = Interior
        fields = ['name', 'description', 'room']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control py-1',
            }),
            'description': Textarea(attrs={
                'class': 'form-control py-1',
                'cols': '40',
                'rows': '7'
            }),
            'room': FileInput(attrs={
                'class': 'form-control py-1',
            }),
        }