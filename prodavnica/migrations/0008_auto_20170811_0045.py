# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodavnica', '0007_auto_20170811_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slika',
            name='slika',
        ),
        migrations.AddField(
            model_name='slika',
            name='lokacija',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
