# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-13 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_studentpaymentdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpaymentdetail',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_name', to='students.Students'),
        ),
    ]
