# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0019_auto_20170802_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='chainwork',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='node',
            name='difficulty',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
    ]
