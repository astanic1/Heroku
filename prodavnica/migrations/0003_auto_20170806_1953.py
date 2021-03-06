# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prodavnica', '0002_auto_20170806_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='artikal',
            name='kategorija',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodavnica.Kategorija'),
        ),
    ]
