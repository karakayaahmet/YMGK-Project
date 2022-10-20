from django.shortcuts import path
from . import views

urlpatterns = [
    path("", views.login),
    path("kayit-ol", views.kayit_ol),
]