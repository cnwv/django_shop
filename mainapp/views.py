from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator
from django.core.cache import cache


def index(request):
    title = {'title': 'main'}
    return render(request, 'mainapp/index.html', title)


def products(request, category_id=None, page=1):
    if category_id:
        products = cache.get(f'products_by_category_{category_id}')
        if products is None:
            products = Product.objects.filter(category_id=category_id).order_by('-price')
            cache.set(f'products_by_category_{category_id}_page{page}', products)
    else:
        products = cache.get(f'products_page{page}')
        if products is None:
            products = Product.objects.all().order_by('-price')
            cache.set(f'products_page{page}', products)
    paginator = Paginator(object_list=products, per_page=3)
    products_paginator = paginator.page(page)
    categories = cache.get('categories')
    if categories is None:
        categories = ProductCategory.objects.all()
        cache.set('categories', categories)
    context = {'categories': categories, 'products': products_paginator}
    return render(request, 'mainapp/products.html', context)
