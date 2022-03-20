from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse
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
        return render(request, 'main/room.html', {'room': room, 'interior': interior})

    @method_decorator(login_required)
    def post(self, request, id):
        if request.POST.get('delete'):
            return redirect(reverse('delete_room', kwargs={'id': id}))
        if request.POST.get('update'):
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
        room = get_object_or_404(Room, id=id)
        if room.name == 'Склад':
            return redirect('cabinets')
        room.exist = False
        room.save()
        store, created = Room.objects.get_or_create(name='Склад', defaults={
            'description': 'Помещение для хранения предметов, непривязанных к комнате'})
        interior = Interior.objects.filter(room__id=id)
        for el in interior:
            el.room = store
            el.save()
            Displacement.objects.create(object=el, from_room=room, to_room=store)
        return redirect('cabinets')


class DisplacementView(View):

    @method_decorator(login_required)
    def post(self, request):
        id = request.POST.get('id')
        if id is None:
            displace = Displacement.objects.all()
        else:
            displace = Displacement.objects.filter(object__id=id)
        return render(request, 'main/displacement.html', {'displace': displace, 'id': id})

    @method_decorator(login_required)
    def get(self, request):
        id = None
        displace = Displacement.objects.all()
        return render(request, 'main/displacement.html', {'displace': displace, 'id': id})


class ListInterior(ListView):
    model = Interior
    template_name = 'main/stock.html'

    def get_queryset(self):
        return Interior.objects.filter(exist=True)


class DetailInterior(View):
    context = {}

    def get(self, request, id):
        interior = get_object_or_404(Interior, id=id, exist=True)
        self.context['object'] = interior
        self.context['displace'] = Displacement.objects.filter(object=interior)
        return render(request, 'main/detail_interior.html', self.context)

    @method_decorator(login_required)
    def post(self, request, id):
        if request.POST.get('delete'):
            return redirect(reverse('stock_delete', kwargs={'id': id}))
        if request.POST.get('update'):
            return redirect(reverse('stock_update', kwargs={'id': id}))


class UpdateInterior(UpdateView):
    model = Interior
    form_class = InteriorForm
    template_name = 'main/update_interior.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return super().get_queryset().filter(exist=True)

    def form_valid(self, form):
        self.object = form.save()
        displacement = Displacement.objects.filter(object=self.object).last()
        if self.object.room != displacement.to_room:
            displace = Displacement(object=self.object, from_room=displacement.to_room,
                                    to_room=self.object.room)
            displace.save()
        return redirect('stock_detail', self.kwargs['id'])


class CreateInterior(CreateView):
    model = Interior
    form_class = InteriorForm
    template_name = 'main/create_interior.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return super().get_queryset().filter(exist=True)

    def form_valid(self, form):
        self.object = form.save()
        displacement = Displacement(object=self.object, to_room=self.object.room)
        displacement.save()
        return redirect('stock')


class DeleteInterior(View):
    @method_decorator(login_required)
    def get(self, request, id):
        interior = get_object_or_404(Interior, id=id)
        interior.exist = False
        interior.save()
        return redirect('stock')
