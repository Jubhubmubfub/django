# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reviews',
            field=models.ManyToManyField(null=True, to='reviews.Review'),
        ),
    ]