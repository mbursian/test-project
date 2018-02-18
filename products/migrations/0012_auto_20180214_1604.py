# -*- coding: utf-8 -*-
# Generated by Django 2.0.2 on 2018-02-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180213_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complexproduct',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='short_description',
        ),
        migrations.AddField(
            model_name='complexproduct',
            name='delivery',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.CharField(blank=True, default=None, max_length=240, null=True),
        ),
    ]
