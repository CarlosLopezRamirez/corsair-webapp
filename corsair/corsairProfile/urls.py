from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'corsairProfile'
urlpatterns = [
    path('', views.directory),
]
