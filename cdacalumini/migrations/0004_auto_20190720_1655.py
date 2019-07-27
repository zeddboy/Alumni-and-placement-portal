# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-20 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdacalumini', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semail', models.CharField(max_length=50)),
                ('profile', models.CharField(max_length=50)),
                ('organisation', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('duration', models.CharField(max_length=2)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semail', models.CharField(max_length=50)),
                ('profile', models.CharField(max_length=50)),
                ('organisation', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('startd', models.DateField()),
                ('endd', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('semail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semail', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('organisation', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('duration', models.CharField(max_length=2)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='sid',
            new_name='semail',
        ),
    ]
