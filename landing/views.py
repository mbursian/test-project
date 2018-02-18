from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from news.models import *
from we.models import *

def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__on_main=True)
    complex_products_images = ComplexProductImage.objects.filter(is_active=True, is_main=True, complex_product__is_active=True, complex_product__on_main=True)
    return render(request, 'landing/home.html', locals())


def catalog (request):
    categories = ProductCategory.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    complex_products_images = ComplexProductImage.objects.filter(is_active=True, is_main=True, complex_product__is_active=True)
    return render(request, 'landing/catalog.html', locals())


def news (request):
    news = News.objects.filter().order_by('-created')
    return render(request, 'news/news.html', locals())


def we (request):
    we = We.objects.filter().order_by('-created')
    return render(request, 'landing/we.html', locals())