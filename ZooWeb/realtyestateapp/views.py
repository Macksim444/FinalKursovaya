from lib2to3.fixes.fix_input import context
from multiprocessing.managers import BaseManager

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


from goods.models import Categories

def index(request):

    categories: BaseManager[Categories] = Categories.objects.all()
    context: dict[str, str] = {
        'title': 'Home - Главная',
        'content': "Зоопарк Koala's smile",
        'categories': categories
    }
    return render(request, 'realtyestateapp/index.html',  context)


def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': "О нас",
        "text_on_page": "Наш зоопарк является жемчужиной такого города, как Северск. Мы распологаемся по адресу: ул.Профсоюзная, д.22. Ждем вас в гости"
    }
    return render(request, 'realtyestateapp/about.html', context)


def catalog(request):
    return render(request, 'realtyestateapp/catalog.html')

def product(request):
    return render(request, 'realtyestateapp/product.html')


