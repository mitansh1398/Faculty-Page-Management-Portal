# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0011_auto_20171111_1242'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AlterField(
            model_name='publication',
            name='published',
            field=models.CharField(choices=[('Journal', 'journal'), ('Conference', 'conference')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor')], default='', max_length=50),
        ),
    ]