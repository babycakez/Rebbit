# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rebbit', '0002_remove_sub_rebb_contributors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sub_reb',
            new_name='subreddit',
        ),
    ]
