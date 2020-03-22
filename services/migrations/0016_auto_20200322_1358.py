# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-22 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20200322_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetails',
            name='amendments',
            field=models.CharField(blank=True, choices=[('Amemdments: 3', '3'), ('Amemdments: 5', '5'), ('Amemdments: 7', '7'), ('Amemdments: UNLIMITED', 'UNLIMITED')], default=' ', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='servicedetails',
            name='contents',
            field=models.CharField(default=' ', max_length=254),
        ),
        migrations.AlterField(
            model_name='servicedetails',
            name='delivery_time',
            field=models.CharField(blank=True, choices=[('Delivery Time: 30 Days', '30 Days'), ('Delivery Time: 28 Days', '28 Days'), ('Delivery Time: 21 Days', '21 Days'), ('Delivery Time: 14 Days', '14 Days'), ('Delivery Time: 7 Days', '7 Days'), ('Delivery Time: 3 Days', '3 Days')], default=' ', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='servicedetails',
            name='title',
            field=models.CharField(default=' ', max_length=254),
        ),
    ]
