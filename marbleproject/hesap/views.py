from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, "hesap/login.html")

def kayit_ol(request):
    return render(request, "hesap/kayit_ol.html")

# Create your views here.
