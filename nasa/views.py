from django.shortcuts import render
from .models import Image


def index(request):
    photos = Image.objects.all()
    context = {
        'photos': photos
    }
    return render(request, 'nasa/index.html', context=context)
