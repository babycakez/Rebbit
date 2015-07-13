# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rebbit', '0003_auto_20150712_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='x',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
