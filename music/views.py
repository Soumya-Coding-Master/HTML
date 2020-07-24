from django.shortcuts import render
from .models import Songs
def index(request):
    s=Songs()
    s.img = 'youtube1.jpg'
    return render(request, 'index.html', {'hola': s})
# Create your views here.
