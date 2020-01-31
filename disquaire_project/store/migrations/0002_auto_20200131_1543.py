# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-01-31 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'disque'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'artiste'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'réservation'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'prospect'},
        ),
        migrations.AlterField(
            model_name='album',
            name='available',
            field=models.BooleanField(default=True, verbose_name='disponible'),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de création'),
        ),
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.TextField(verbose_name="URL de l'image"),
        ),
        migrations.AlterField(
            model_name='album',
            name='reference',
            field=models.IntegerField(null=True, verbose_name='référence'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=200, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contacted',
            field=models.BooleanField(default=False, verbose_name='demande traitée ?'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="date d'envoi"),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nom'),
        ),
    ]
