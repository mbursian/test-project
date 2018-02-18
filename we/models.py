# -*- coding: utf-8 -*-
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class We (models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    content = RichTextUploadingField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'О Нас'
        verbose_name_plural = 'О Нас'

