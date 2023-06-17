from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import PostForm, ContactForm, CreateProductForm
from catalog.models import Product, Post, Contact


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }


class ProductDetailView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    form_class = CreateProductForm
    # fields = ('product_name', 'description', 'image', 'purchase_price', 'category')
    success_url = reverse_lazy('catalog:product_list')

    # def form_valid(self, form: CreateProductForm) -> HttpResponseRedirect:
    #     """
    #     Обрабатывает форму, если она валидна,
    #     сохраняет товар и перенаправляет на страницу деталей товара.
    #     """
    #     product = form.save(commit=False)
    #     product.created_by = self.request.user
    #     product.save()
    #
    #     messages.success(self.request, 'Товар успешно добавлен')
    #     return HttpResponseRedirect(reverse('catalog:product_detail', args=[product.id]))


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Посты'
    }


class DetailPost(DetailView):
    model = Post

    def get_object(self, queryset=None):
        object = Post.objects.get(pk=self.kwargs['pk'])
        if object:
            object.count_views += 1
            object.save()
        return object


class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('catalog:post_list')
    form_class = PostForm


class PostUpdate(UpdateView):
    model = Post
    template_name = 'catalog/update_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('catalog:post_detail', kwargs={'pk': self.kwargs['pk']})


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:post_list')


class ContactListView(ListView):
    model = Contact
    extra_context = {
        'title': 'Контакты'
    }


class ContactCreate(CreateView):
    model = Contact

    form_class = ContactForm
    template_name = 'catalog/contact_create.html'
    success_url = reverse_lazy('catalog:contact_list')

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
