from django.contrib import admin
from django.urls import path
from galeria.views import index, imagem, search

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<str:imagem_date>', imagem, name="imagem"),
    path("search/", search, name="search"),
]
