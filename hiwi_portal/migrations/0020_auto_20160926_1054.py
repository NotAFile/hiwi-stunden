# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 10:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiwi_portal', '0019_remove_worklog_overwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillerworkdustactivity',
            name='avg_length',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='fixedworkdustactivity',
            name='avg_length',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='hours',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
