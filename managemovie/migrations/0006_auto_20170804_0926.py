# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managemovie', '0005_auto_20170802_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='movie',
            name='logo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
