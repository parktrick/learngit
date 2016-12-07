# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[(0, '普通用户'), (1, '高级用户')])),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user_info',
            field=models.ManyToManyField(to='app01.UserInfo'),
        ),
        migrations.AddField(
            model_name='host',
            name='user_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup'),
        ),
    ]
