from django.contrib import admin
from .models import Category, Product


class CategoryConfig(admin.ModelAdmin):
    fields = ('name', 'slug_category')
    list_display = ('name', )
    prepopulated_fields = {'slug_category': ('name',)}


admin.site.register(Category, CategoryConfig)


class ProductConfig(admin.ModelAdmin):
    fields = ('name', 'category', 'price', 'slug_product')
    list_display = ('name', 'category', 'price')
    prepopulated_fields = {'slug_product': ('name',)}


admin.site.register(Product, ProductConfig)
