import os

from django.urls import reverse
from django.views import View
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def mainpg(request):
    return render(request, 'main/mainpg.html')

def stock(request):
    return render(request, 'main/stock.html')

def faqs(request):
    return render(request, 'main/faqs.html')

class CabinetsView(View):

    def post(self, request):
        id = request.POST.get('id')
        return redirect(reverse('room', kwargs={'id': id}))

    def get(self, request):
        rooms = Room.objects.exclude(exist=False)
        return render(request, 'main/cabinets.html', {'rooms': rooms})

class RoomView(View):

    def get(self, request, id):
        rooms = Room.objects.exclude(exist=False)
        room = get_object_or_404(rooms, id=id)
        interior = Interior.objects.filter(room_id=id, exist=True)
        return render(request, 'main/room.html', {'room': room, 'interior':interior})

    @method_decorator(login_required)
    def post(self, request, id):
        if (request.POST.get('delete')):
            return redirect(reverse('delete_room', kwargs={'id': id}))
        if (request.POST.get('update')):
            return redirect(reverse('update_room', kwargs={'id': id}))

class CreateRoomView(View):

    @method_decorator(login_required)
    def post(self, request):
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cabinets')
        else:
            error = 'Ошибка добавления записи'
            form = RoomForm()
            return render(request, 'main/create_room.html', {'form': form, 'error': error})

    @method_decorator(login_required)
    def get(self, request):
        form = RoomForm()
        error = ''
        return render(request, 'main/create_room.html', {'form': form, 'error': error})

class UpdateRoomView(View):

    @method_decorator(login_required)
    def post(self, request, id):
        room = get_object_or_404(Room, id=id)
        try:
            room.name = request.POST.get('name')
            room.description = request.POST.get('description')
            if request.FILES.get('image'):
                if room.image:
                    storage, path = room.image.storage, room.image.path
                    room.image = request.FILES.get('image')
                    storage.delete(path)
                else:
                    room.image = request.FILES.get('image')
            room.save()
            return redirect(reverse('room', kwargs={'id': id}))
        except:
            error = 'Ошибка редактирования комнаты'
            return render(request, 'main/update_room.html', {'room': room, 'error': error})

    @method_decorator(login_required)
    def get(self, request, id):
        rooms = Room.objects.exclude(exist=False)
        room = get_object_or_404(rooms, id=id)
        return render(request, 'main/update_room.html', {'room': room})

class DeleteRoomView(View):

    @method_decorator(login_required)
    def get(self, request, id):
        room = Room.objects.get(id=id)
        room.exist = 0
        room.save()
        return redirect('cabinets')

class DisplacementView(View):

    @method_decorator(login_required)
    def post(self, request):
        id = request.POST.get('id')
        if id == None:
            displace = Displacement.objects.all()
        else:
            displace = Displacement.objects.filter(object__id=id)
        return render(request, 'main/displacement.html', {'displace': displace, 'id': id})

    @method_decorator(login_required)
    def get(self, request):
        id = None
        displace = Displacement.objects.all()
        return render(request, 'main/displacement.html', {'displace': displace, 'id': id})