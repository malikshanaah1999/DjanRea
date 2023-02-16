from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # Thx to this 'name' attr., you will be able to access a specific path by its name...later on.
    path('room/', views.room, name = "room" ),
]