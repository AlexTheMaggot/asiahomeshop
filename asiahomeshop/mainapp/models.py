from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    slug_category = models.SlugField(verbose_name='URL (добавляется автоматически)', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    slug_product = models.SlugField(verbose_name='URL (добавляется автоматически)', unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'