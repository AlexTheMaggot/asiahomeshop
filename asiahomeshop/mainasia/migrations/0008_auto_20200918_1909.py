# Generated by Django 3.0 on 2020-09-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainasia', '0007_auto_20200918_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/products/', verbose_name='Изображение 2'),
        ),
    ]