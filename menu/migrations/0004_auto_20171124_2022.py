# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 02:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_plato_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='union',
            old_name='Menu',
            new_name='menu',
        ),
    ]