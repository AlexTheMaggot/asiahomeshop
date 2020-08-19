# Generated by Django 3.1 on 2020-08-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_product_price_disc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_disc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена со скидкой'),
        ),
    ]