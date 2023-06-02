from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)

# from catalog.models import Product
#
#
# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Главная'
#     }
#
#     return render(request, 'catalog/product_list.html', context)
#
