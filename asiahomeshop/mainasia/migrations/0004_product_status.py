# Generated by Django 3.0 on 2020-09-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainasia', '0003_auto_20200830_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
