from django.conf import settings
from django.core.cache import cache

from .models import Category


def get_all_categories():
    """
    Возвращает все категории товаров с использованием кеширования.
    """
    if settings.CACHE_ENABLED:
        categories = cache.get('all_categories')
        if categories is None:
            categories = Category.get_all_categories()
            cache.set('all_categories', categories, 60 * 15)
        return categories
    else:
        return Category.get_all_categories()
