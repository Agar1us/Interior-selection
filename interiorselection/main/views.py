from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from .forms import *
from .models import *
from django.shortcuts import render, redirect


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
        if object == None:
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


class ListObjects(ListView):
    model = Interior
    template_name = 'main/stock.html'

    def get_queryset(self):
        return Interior.objects.filter(exist=True)
