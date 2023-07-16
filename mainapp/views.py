from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
# контроллер = функция
# MVC = Model View Controller
# MVT = Model View Template

def index(request):
    title = {'title': 'main'}
    return render(request, 'mainapp/index.html', title)


def products(request, id=None):
    title = {'title': 'catalog'}
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
