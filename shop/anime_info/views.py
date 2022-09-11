from django.shortcuts import render


# Create your views here.

def info_anime(request):
    return render(request, 'info_anime.html')
