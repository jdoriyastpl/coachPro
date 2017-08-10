# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-06 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('remark', models.TextField(blank=True, null=True)),
                ('subject', models.CharField(max_length=150)),
                ('age', models.PositiveIntegerField(verbose_name='Student Age')),
                ('father_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('adhaar_number', models.PositiveIntegerField()),
                ('course_name', models.ManyToManyField(related_name='student_course', to='courses.Courses')),
            ],
        ),
        migrations.AddField(
            model_name='studentfee',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_name', to='students.Students'),
        ),
    ]