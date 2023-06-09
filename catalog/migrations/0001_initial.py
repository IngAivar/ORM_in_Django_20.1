# Generated by Django 4.2.1 on 2023-05-24 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('category',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='наименование продукта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение (превью)')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='цена за покупку')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('last_modified_date', models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.category', verbose_name='ID категории')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('product_name',),
            },
        ),
    ]
