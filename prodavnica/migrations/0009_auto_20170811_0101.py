# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodavnica', '0008_auto_20170811_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slika',
            name='lokacija',
        ),
        migrations.AddField(
            model_name='slika',
            name='slika',
            field=models.ImageField(default='C:\\Python34\\Scripts\\env_site1\\korisnik.png', upload_to='C:\\Python34\\Scripts\\env_site1'),
        ),
    ]
