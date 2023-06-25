from django.shortcuts import render


# Create your views here.
# контроллер = функция
# MVC = Model View Controller
# MVT = Model View Template

def index(request):
    title = {'title': 'main'}
    return render(request, 'mainapp/index.html', title)


def products(request):
    title = {'title': 'catalog'}
    return render(request, 'mainapp/products.html')


def test_context(request):
    context = {
        'title': 'test Context',
        'header': 'Йоу',
        'username': 'Паша Техник',
        'products': [{'name': 'Бокс слим блок лого худи', 'price': '7000'},
                     {'name': 'Лонгслив свивной', 'price': '1300'},
                     {'name': 'Тишка', 'price': '4500'},
                     {'name': 'Тули', 'price': '1000000'},
                     ]
    }
    return render(request, 'mainapp/context.html', context)
