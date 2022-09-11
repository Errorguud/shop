from django.shortcuts import render


def index_anime(request):
    return render(request, 'index.html')


