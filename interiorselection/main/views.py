from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


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


