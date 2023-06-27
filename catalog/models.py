from typing import Optional

from django.db import models
from transliterate import translit

from user.models import CustomUser

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.category} \n {self.description} \n'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта', **NULLABLE)
    image = models.ImageField(upload_to='product/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='ID категории', on_delete=models.PROTECT, **NULLABLE)
    purchase_price = models.IntegerField(verbose_name='цена за покупку', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Кем создан', default=1)
    is_published = models.BooleanField(verbose_name='Опубликован', default=False)

    def __str__(self):
        return f'{self.product_name} \n {self.description} \n {self.purchase_price}$ \n'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)

    def get_active_version(self) -> Optional['Version']:
        """
        Возвращает активную версию товара, если она существует.
        Если активная версия не найдена, возвращает None
        """
        return self.version.filter(is_current_version=True).first()

    @classmethod
    def get_unpublished_products(cls) -> models.QuerySet:
        """
        Возвращает все неопубликованные товары.

        :return: QuerySet с неопубликованными товарами
        """
        return cls.objects.filter(is_published=False)


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField()
    site = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.phone} | {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    slug = models.CharField(max_length=30, verbose_name='Слаг')
    content = models.TextField(verbose_name='Контент')
    preview = models.ImageField(upload_to='media', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=False, verbose_name='Опубликованно')
    count_views = models.IntegerField(default=0, verbose_name='Коллчество просмотров')

    def save(self, *args, **kwargs):
        self.slug = translit(self.title, language_code='ru', reversed=True)
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.title} | {self.content[:30]}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Version(models.Model):
    """
    Модель, описывающая версию товара.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version', verbose_name='Продукт')
    version_number = models.CharField(max_length=100, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='Текущая версия')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        db_table = 'versions'

    def __str__(self):
        return f"{self.version_number}: {self.version_name}"
