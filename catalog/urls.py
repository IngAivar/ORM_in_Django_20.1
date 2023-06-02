
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts

# from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),

    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
]
