from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'galeria/index.html')


def imagem(request: HttpRequest) -> HttpResponse:
    return render(request, 'galeria/imagem.html')