# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('mail', models.CharField(max_length=32)),
                ('qq', models.CharField(max_length=32)),
                ('tel', models.CharField(max_length=32)),
            ],
        ),
    ]