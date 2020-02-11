# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-02-11 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20200211_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='refplagehoraire',
            name='jour',
            field=models.CharField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')], default=1, max_length=25, verbose_name='Jours du marché'),
            preserve_default=False,
        ),
    ]