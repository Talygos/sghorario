# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-22 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaHorario', '0002_remove_matrizcurricular_numeroperiodos'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrizcurricular',
            name='nomeMatriz',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]