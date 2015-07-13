# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Rebbit', '0007_auto_20150712_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_rebb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 9, 0, 48, 556927, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
