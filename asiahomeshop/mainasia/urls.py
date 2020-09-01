from django.urls import path
from . import views
from .views import PostDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug_product>', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('blog/', views.blog, name='blog'),
    path('singlepro/', views.singlepro, name='singlepro'),
    path('blogsingle/', views.blogsingle, name='blogsingle'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]