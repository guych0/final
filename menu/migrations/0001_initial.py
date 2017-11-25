# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=30)),
                ('ingrediente', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Plato')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='platio',
            field=models.ManyToManyField(through='menu.Union', to='menu.Plato'),
        ),
    ]
