# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='university',
            new_name='school',
        ),
    ]
