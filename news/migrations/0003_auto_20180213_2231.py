# Generated by Django 2.0.2 on 2018-02-13 19:31

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180213_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None),
        ),
    ]
