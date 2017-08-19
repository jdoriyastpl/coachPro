# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20170819_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpaymentdetail',
            name='fee_by',
            field=models.CharField(blank=True, choices=[('monthly_fee', 'Monthly'), ('quarterly_fee', 'Quarterly'), ('yearly_fee', 'YEARLY')], default='monthly_fee', max_length=15, verbose_name='Choose fee options'),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_Id',
            field=models.CharField(default='STU20178IXM5ZP', max_length=200),
        ),
    ]
