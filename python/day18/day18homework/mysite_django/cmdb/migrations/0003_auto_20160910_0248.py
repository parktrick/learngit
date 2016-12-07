# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_hostinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='nid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='port',
            field=models.IntegerField(default=80),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='status',
            field=models.CharField(max_length=32),
        ),
    ]