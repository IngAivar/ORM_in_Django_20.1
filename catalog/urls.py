
from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactListView, PostListView, ProductDetailView, ProductCreate, \
    ContactCreate, DetailPost, PostCreate, PostUpdate, DeletePost, ProductUpdateView, ProductDeleteView, \
    UnpublishedProductListView

# from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail_product/<int:pk>/', cache_page(60 * 2)(ProductDetailView.as_view()), name='product_detail'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('create_product/', never_cache(ProductCreate.as_view()), name='product_form'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('unpublished/', UnpublishedProductListView.as_view(), name='unpublished_products'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('contacts/create_contact', ContactCreate.as_view(), name='contact_create'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('detail_post/<int:pk>/', DetailPost.as_view(), name='post_detail'),
    path('create_post/', PostCreate.as_view(), name='post_form'),
    path('update_post/<int:pk>/', PostUpdate.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name='delete_post'),

    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
]
