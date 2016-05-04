# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vanillablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='list',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
