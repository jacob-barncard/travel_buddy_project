# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]
