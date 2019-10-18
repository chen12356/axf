# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-11 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Axf_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32)),
                ('u_password', models.CharField(max_length=256)),
                ('u_email', models.CharField(max_length=64)),
                ('u_icon', models.ImageField(upload_to='icons')),
                ('u_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
