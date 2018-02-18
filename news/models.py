from django.db import models
from products.models import Product
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save


class News(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    content_preview = RichTextUploadingField(blank=True, default=None)
    content = RichTextUploadingField(blank=True, default=None)
    actual_for =models.CharField(max_length=64, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class ProductReview(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    content_preview = RichTextUploadingField(blank=True, default=None)
    content = RichTextUploadingField(blank=True, default=None)
    actual_for = models.CharField(max_length=64, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Обзор товара'
        verbose_name_plural = 'Обзоры товара'