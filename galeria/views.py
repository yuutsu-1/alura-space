from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.http import HttpResponse, HttpRequest
from handlers.imageAPI import ImageAPI
from datetime import datetime, timedelta
from galeria.models import NASAImage

def index(request):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=9)
    cache_key = f"nasa_images_{start_date}_{end_date}"
    
    images = cache.get(cache_key)
    
    if not images:
        reqImage = ImageAPI()
        reqImage.fetch(start_date=start_date, end_date=end_date)
        
        images = NASAImage.objects.all().order_by("-date")
        cache.set(cache_key, images, timeout=3600)
    
                
    return render(request, 'galeria/index.html', {"images": images})

def imagem(request: HttpRequest, imagem_date) -> HttpResponse:
    item = get_object_or_404(NASAImage, pk=imagem_date)
    
    return render(request, 'galeria/imagem.html', {"item": item})

def search(request: HttpRequest) -> HttpResponse:
    if not "query" in request.GET:
        return render(request, 'galeria/index.html', {"images": NASAImage.objects.none()})

    query = request.GET.get("query")
    
    print(query)
    if query:
        images = NASAImage.objects.filter(title__icontains=query)
    else:
        images = NASAImage.objects.none()
    
    return render(request, 'galeria/index.html', {"images": images})