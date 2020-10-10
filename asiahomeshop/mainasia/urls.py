from django.urls import path
from . import views
from .views import PostDetailView

app_name = 'mainasia'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug_product>', views.shop, name='product'),
    path('shop/categories/<slug:slug_category>/', views.shop, name='category_view'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('blog/', views.blog, name='blog'),
    path('singlepro/', views.singlepro, name='singlepro'),
    path('blogsingle/', views.blogsingle, name='blogsingle'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('thank-you/', views.thankyou, name='thankyou'),
    path('wrong/', views.wrong, name='wrong'),
]