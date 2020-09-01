from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm
from django.views import View
from .forms import ApplicationsForm
import telebot
from django.core.mail import send_mail
from django.views import View
from blog.models import Post
from django.views.generic import DetailView

bot = telebot.TeleBot("1266052691:AAEQ993zB8P6XCbwluG2HtESTNhCNr75x4s")


def index(request):
    return render(request, 'mainasia/index.html')


def about(request):
    return render(request, 'mainasia/about.html')


def cart(request):
    return render(request, 'mainasia/cart.html')


def contact(request):
    form = ApplicationsForm()
    context = {'form': form}
    return render(request, 'mainasia/contact.html', context)


def blog(request):
    return render(request, 'mainasia/blog.html')


def singlepro(request):
    return render(request, 'mainasia/single_shop.html')


def blogsingle(request):
    return render(request, 'mainasia/blog_single.html')


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
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
            from_email = 'no-reply@bindoors.ru'
            to_email = ['aitofullstackdev@gmail.com', 'aitolivelive@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(-328895642, message)
        return redirect('contact')


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_single.html'


def product(request, slug_product):
    product = get_object_or_404(Product, slug_product__iexact=slug_product)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'mainasia/single_shop.html', context)
