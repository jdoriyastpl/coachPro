# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpaymentdetail',
            name='next_payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentpaymentdetail',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
