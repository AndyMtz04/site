# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-02 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_frontpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontpage',
            name='description',
        ),
    ]
