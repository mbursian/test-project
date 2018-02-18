from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'products/product.html', locals())


def complex_product(request, complex_product_id):
    complex_product = ComplexProduct.objects.get(id=complex_product_id)

    return render(request, 'complex_products/complex_product.html', locals())


def category(request, category_id):
    category = ProductCategory.objects.get(id=category_id)

    return render(request, 'landing/catalog.html', locals())