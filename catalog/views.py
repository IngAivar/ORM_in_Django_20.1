from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Post, Contact


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }


class ProductDetailView(DetailView):
    model = Product


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Посты'
    }


class ContactListView(ListView):
    model = Contact
    extra_context = {
        'title': 'Контакты'
    }

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
