# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreigncurrencyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foreigncurrencyapp.CurrenciesFrom')),
                ('to_currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foreigncurrencyapp.CurrenciesTo')),
            ],
        ),
    ]