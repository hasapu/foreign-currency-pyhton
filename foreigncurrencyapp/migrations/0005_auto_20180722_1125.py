# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreigncurrencyapp', '0004_auto_20180722_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='Rate',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
