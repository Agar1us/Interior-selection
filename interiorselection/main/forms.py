from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileInput, Select


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
            'image': FileInput(attrs={
                'class': 'form-control py-1',
            }),
        }


class InteriorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(InteriorForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(exist=True)

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
            'room': Select(attrs={
                'class': 'form-control py-1',
            }),
        }
