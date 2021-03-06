# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-14 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MarketApp', '0004_auto_20191010_1347'),
        ('UserApp', '0002_axf_user_u_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axf_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_goods_num', models.IntegerField(default=1)),
                ('c_is_select', models.BooleanField(default=True)),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarketApp.Axf_goods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.Axf_user')),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
    ]
