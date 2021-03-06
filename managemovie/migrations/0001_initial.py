# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('producer', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('synopsisa', models.TextField(max_length=300)),
                ('logo', models.CharField(max_length=30)),
                ('trailer', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('file', models.TextField(max_length=300)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managemovie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Starring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managemovie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=50)),
                ('mobile_num', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='bookingseat',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managemovie.Movie'),
        ),
        migrations.AddField(
            model_name='bookingseat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managemovie.User'),
        ),
    ]
