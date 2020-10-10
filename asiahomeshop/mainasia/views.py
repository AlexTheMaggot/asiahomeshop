from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.views import View
from .forms import ApplicationsForm
import telebot
from django.core.mail import send_mail
from blog.models import Post
from django.views.generic import DetailView
# from accounts.forms import LoginForm
# from django.contrib import auth
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.core.paginator import Paginator
from cart.cart import Cart


bot = telebot.TeleBot("1266052691:AAEQ993zB8P6XCbwluG2HtESTNhCNr75x4s")


def index(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'mainasia/index.html', context)


def about(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'mainasia/about.html', context)


def cart(request):
    return render(request, 'mainasia/cart.html')


def contact(request):
    form = ApplicationsForm()
    cart = Cart(request)
    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'mainasia/contact.html', context)


def singlepro(request):
    return render(request, 'mainasia/single_shop.html')


def blogsingle(request):
    return render(request, 'mainasia/blog_single.html')


def shop(request, slug_category=None):
    category = Category.objects.all()
    products = Product.objects.all()
    selected_category = ''
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if slug_category:
        category = Category.objects.all()
        selected_category = get_object_or_404(Category, slug_category=slug_category)
        products = Product.objects.filter(category=selected_category).order_by('-id')
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    context = {
        'cart': cart,
        'products': products,
        'cart_product_form': cart_product_form,
        'category': category,
        'page_obj': page_obj,
    }   
    return render(request, 'mainasia/shop.html', context)


class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            # print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка!'
            from_email = 'assassinaltair@bk.ru'
            to_email = ['aitofullstackdev@gmail.com', 'aitolivelive@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(-328895642, message)
        return redirect('mainasia:contact')


def blog(request):
    posts = Post.objects.all()
    cart = Cart(request)
    context = {
        'posts': posts,
        'cart': cart,
    }
    return render(request, 'blog/blog.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_single.html'


def product(request, slug_product):
    product = get_object_or_404(Product, slug_product__iexact=slug_product)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart,
    }
    return render(request, 'mainasia/single_shop.html', context)


def product_detail(request, id, slug):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, ApplicationsViewlable=True)
    cart = Cart(request)
    context = {
        'product': product,
        'products': products,
        'cart': cart,
    }
    return render(request, 'mainasia/single_shop.html', context)


def login(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'accounts/login.html', context)


def register(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'accounts/register.html', context)


def thankyou(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'mainasia/thank-you.html', context)


def wrong(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'mainasia/wrong.html', context)

