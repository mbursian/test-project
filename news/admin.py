from django.contrib import admin
from .models import *


class ProductReviewAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductReview._meta.fields]

    class Meta:
        model = ProductReview


admin.site.register(ProductReview, ProductReviewAdmin)


class NewsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)