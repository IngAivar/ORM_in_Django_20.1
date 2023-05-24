from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.category} \n {self.description}'

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

    def __str__(self):
        return f'{self.product_name} \n {self.description} \n {self.purchase_price}$'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
