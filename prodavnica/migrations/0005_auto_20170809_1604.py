# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prodavnica', '0004_auto_20170808_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narudzba',
            name='datum_narudzbe',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='datum narudzbe'),
        ),
    ]
