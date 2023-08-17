from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top_sellers.html')


def advertisement_post(request):
    return render(request, 'advertisement_post')


def register(request):
    return render(request, 'register')


def login(request):
    return render(request, 'login')


def profile(request):
    return render(request, 'profile')
