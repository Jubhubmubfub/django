# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20170125_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='reviews.Book'),
            preserve_default=False,
        ),
    ]
