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


def stock(request):
    return render(request, 'main/stock.html')


def faqs(request):
    return render(request, 'main/faqs.html')


def log_reg(request):
    return render(request, 'main/log_reg.html')

def create_room(request):

    if request.method == 'POST':
        form = RoomsForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Rooms.objects.create(**form.cleaned_data)
                return redirect('cabinets')
            except:
                form.add_error(None, 'Ошибка добавления комнаты')
    else:
        form = RoomsForm

    return render(request, 'main/create_room.html', {'form': form })