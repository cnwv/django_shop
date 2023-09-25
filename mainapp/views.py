from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
# контроллер = функция
# MVC = Model View Controller
# MVT = Model View Template

def index(request):
    title = {'title': 'main'}
    return render(request, 'mainapp/index.html', title)


def products(request, category_id=None):
    context = {
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
