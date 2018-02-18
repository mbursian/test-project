from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class ComplexProduct(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    delivery = models.CharField(max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=True, default=None)
    is_active = models.BooleanField(default=True)
    on_main = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    opt_desc = RichTextUploadingField(blank=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Сложный товар'
        verbose_name_plural = 'Сложные товары'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    delivery = models.CharField(max_length=240, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=True, default=None)
    is_active = models.BooleanField(default=True)
    on_main = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    complex_product = models.ForeignKey(ComplexProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    opt_desc = RichTextUploadingField(blank=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товара'


class ComplexProductImage(models.Model):
    complex_product = models.ForeignKey(ComplexProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='complex_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография сложного товара'
        verbose_name_plural = 'Фотографии сложного товара'

