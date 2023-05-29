from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)

