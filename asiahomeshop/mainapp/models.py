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

    RATE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]

    name = models.CharField(verbose_name='Имя', max_length=200)
    img1 = models.ImageField(verbose_name='Изображение 1', upload_to='static/img/products/')
    img2 = models.ImageField(verbose_name='Изображение 2', upload_to='static/img/products/')
    slug_product = models.SlugField(verbose_name='URL (добавляется автоматически)', unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    price_disc = models.DecimalField(verbose_name='Цена со скидкой', max_digits=7, decimal_places=2, null=True,
                                     blank=True)
    discount = models.DecimalField(verbose_name='Размер скидки', max_digits=2, decimal_places=0, null=True, blank=True)
    new = models.BooleanField(verbose_name='Новый товар')
    rating = models.CharField(verbose_name='Рейтинг', max_length=1, choices=RATE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'