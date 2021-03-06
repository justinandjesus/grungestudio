# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-24 14:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grunge', '0008_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuExcSignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.CharField(max_length=1000)),
                ('message', models.TextField(max_length=100000)),
                ('link', models.CharField(max_length=1000)),
                ('file', models.FileField(max_length=500, upload_to=b'')),
            ],
        ),
    ]
