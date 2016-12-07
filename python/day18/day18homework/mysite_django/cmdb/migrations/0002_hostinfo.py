# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('port', models.IntegerField(max_length=4)),
                ('status', models.IntegerField(choices=[(0, '下线'), (1, '上线')], max_length=2)),
            ],
        ),
    ]
