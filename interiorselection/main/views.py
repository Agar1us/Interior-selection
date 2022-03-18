from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, UpdateView
from django.urls import reverse
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def mainpg(request):
    return render(request, 'main/mainpg.html')


def cabinets(request):
    return render(request, 'main/cabinets.html')


def faqs(request):
    return render(request, 'main/faqs.html')


class DisplacementView(View):
    # @method_decorator(login_required)
    def post(self, request):
        object = request.POST.get('object')
        if object is None:
            displace = Displacement.objects.all()
        else:
            displace = Displacement.objects.filter(object__name=object)
        return render(request, 'main/displacement.html', {'displace': displace, 'object': object})

    # @method_decorator(login_required)
    def get(self, request):
        object = None
        displace = Displacement.objects.all()
        return render(request, 'main/displacement.html', {'displace': displace, 'object': object})


class CreateRoomView(View):
    # @method_decorator(login_required)
    def post(self, request):
        error = ''
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cabinets')
        else:
            error = 'Ошибка добавления записи'
            form = RoomForm()
            return render(request, 'main/create_room.html', {'form': form, 'error': error})

    # @method_decorator(login_required)
    def get(self, request):
        form = RoomForm()
        error = ''
        return render(request, 'main/create_room.html', {'form': form, 'error': error})


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
        print(self.object.room, displacement.to_room)
        if self.object.room != displacement.to_room:
            displace = Displacement(object=self.object, from_room=displacement.to_room,
                                        to_room=self.object.room)
            displace.save()
        return redirect('stock_detail', self.kwargs['id'])


class DeleteInterior(View):
    def get(self, request, id):
        interior = get_object_or_404(Interior, id=id)
        interior.exist = False
        interior.save()
        return redirect('stock')
