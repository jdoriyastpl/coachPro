# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_Id',
            field=models.CharField(default='STU20185X9ZLVM', max_length=200),
        ),
    ]