from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from shop_index.models import Product


def shop_andex_one(request):
    pr = Product.objects.all
    return render(request, 'shop_one.html', {'pr': pr})
