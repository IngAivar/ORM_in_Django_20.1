
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactListView, PostListView, ProductDetailView

# from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail_product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('post_list/', PostListView.as_view(), name='post_list'),

    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
]
