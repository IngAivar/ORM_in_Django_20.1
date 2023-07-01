from typing import Any, Dict

from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import PostForm, ContactForm, CreateProductForm, ProductVersionFormSet
from catalog.models import Product, Post, Contact, Category
from catalog.services import get_all_categories
from permissions.user_permission import CreatorAccessMixin, ModeratorAccessMixin, ModeratorOrCreatorMixin


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """
        Возвращает контекст данных для шаблона списка товаров,
        включая категории и текущую выбранную категорию.
        """
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get('category')
        context['categories'] = get_all_categories()
        if category_id:
            context['category'] = Category.get_category_by_id(category_id=category_id)
        else:
            context['category'] = 'Все'

        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    form_class = CreateProductForm
    # fields = ('product_name', 'description', 'image', 'purchase_price', 'category')
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form: CreateProductForm) -> HttpResponseRedirect:
        """
        Обрабатывает форму, если она валидна,
        сохраняет товар и перенаправляет на страницу деталей товара.
        """
        product = form.save(commit=False)
        product.created_by = self.request.user
        product.save()

        messages.success(self.request, 'Товар успешно добавлен')
        return HttpResponseRedirect(reverse('catalog:product_detail', args=[product.id]))

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """
        Получает и возвращает контекст данных для шаблона создания товара,
        включая информацию о действии.
        """
        context = super().get_context_data(**kwargs)
        context['action'] = 'Создать'
        return context


class ProductUpdateView(ModeratorOrCreatorMixin, UpdateView):
    """
    Представление для редактирования существующего товара.
    """
    model = Product
    form_class = CreateProductForm

    def form_valid(self, form: CreateProductForm) -> HttpResponseRedirect:
        """
        Обрабатывает форму, если она валидна, сохраняет товар и версии товара и
        перенаправляет на страницу редактирования товара.
        """
        product = form.save()
        context = self.get_context_data()
        versions = context.get('versions')

        if versions.is_valid():
            versions.instance = product
            versions.save()
            messages.success(self.request, 'Товар обновлён')
            return HttpResponseRedirect(reverse('catalog:update_product', args=[product.id]))
        else:
            error_message = versions.non_form_errors()
            messages.error(self.request, error_message)
            return self.form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Возвращает контекст данных для шаблона редактирования товара,
        включая формсет версий и информацию о действии.
        """
        context = super().get_context_data(**kwargs)
        context['versions'] = self.get_versions_formset()
        context['action'] = 'Редактировать'
        return context

    def get_versions_formset(self) -> ProductVersionFormSet:
        """
        Возвращает экземпляр формсета версий товара.
        """
        if self.request.POST:
            return ProductVersionFormSet(self.request.POST, instance=self.object)
        else:
            return ProductVersionFormSet(instance=self.object)


class ProductDeleteView(CreatorAccessMixin, DeleteView):
    """
    Представление для удаления существующего товара.
    """
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def delete(self, request, *args, **kwargs):
        """
        Удаляет товар и перенаправляет на страницу списка товаров.
        """
        self.object = self.get_object()

        message = f'Товар "{self.object.title}" удалён'
        messages.success(request, message)

        return HttpResponseRedirect(self.get_success_url())


class UnpublishedProductListView(ModeratorAccessMixin, ListView):
    """
    Представление для списка неопубликованных товаров.
    Настроена пагинация.
    На одной странице отображается 4 товара.
    """
    template_name = 'catalog/products.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Product]:
        """
        Получает и возвращает queryset неопубликованных товаров.
        """
        return Product.get_unpublished_products()

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """
        Получает и возвращает контекст данных для шаблона.
        """
        context = super().get_context_data(**kwargs)
        context['header'] = 'Неопубликованные товары'
        return context


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
