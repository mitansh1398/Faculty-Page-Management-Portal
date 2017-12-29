# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0002_auto_20171110_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('1', 'Completed'), ('0', 'ongoing')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('professor', 'Professor'), ('assistant professor', 'Assistant Professor'), ('associate professor', 'Associate Professor')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_month',
            field=models.CharField(choices=[('apr', 'April'), ('jul', 'July'), ('aug', 'August'), ('jun', 'June'), ('feb', 'February'), ('jan', 'January'), ('dec', 'December'), ('oct', 'October'), ('may', 'May'), ('mar', 'March'), ('nov', 'November'), ('sep', 'September')], max_length=50),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_month',
            field=models.CharField(choices=[('apr', 'April'), ('jul', 'July'), ('aug', 'August'), ('jun', 'June'), ('feb', 'February'), ('jan', 'January'), ('dec', 'December'), ('oct', 'October'), ('may', 'May'), ('mar', 'March'), ('nov', 'November'), ('sep', 'September')], max_length=50),
        ),
    ]