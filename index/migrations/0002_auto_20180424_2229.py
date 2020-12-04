# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-24 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excel',
            options={'verbose_name': '\u8868\u5185\u5bb9', 'verbose_name_plural': '\u8868\u5185\u5bb9'},
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ['add_date'], 'verbose_name': '\u5217\u540d', 'verbose_name_plural': '\u5217\u540d'},
        ),
        migrations.AddField(
            model_name='field',
            name='add_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='excel',
            name='li_ctx',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='\u8be5\u5217\u5185\u5bb9'),
        ),
    ]
