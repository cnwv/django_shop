from django.shortcuts import render


# Create your views here.
# котроллер = функция
# MVC = Model View Controller
# MVT = Model View Template

def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, '/mainapp/products.html')
