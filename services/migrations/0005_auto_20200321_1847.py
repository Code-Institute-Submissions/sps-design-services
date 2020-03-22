# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-21 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20200321_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetails',
            name='amendments',
            field=models.CharField(choices=[(3, '3'), (5, '5'), (7, '7'), ('NA', 'Not Applicable')], default='NA', max_length=254),
        ),
        migrations.AlterField(
            model_name='servicedetails',
            name='delivery_time',
            field=models.CharField(choices=[(30, '30'), (28, '28'), (21, '21'), (14, '14'), (7, '7'), (3, '3'), ('NA', 'Not Applicable')], default='NA', max_length=254),
        ),
    ]
