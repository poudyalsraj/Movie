# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managemovie', '0002_auto_20170731_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='logo',
            field=models.FileField(max_length=30, upload_to=''),
        ),
    ]