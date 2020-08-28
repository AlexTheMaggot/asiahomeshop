from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug_product>', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('singlepro/', views.singlepro, name='singlepro'),
    path('blogsingle/', views.blogsingle, name='blogsingle'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
]