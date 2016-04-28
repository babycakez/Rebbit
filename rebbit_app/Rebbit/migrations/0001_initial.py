# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=1000)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CommentVoting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30)),
                ('rpost', models.CharField(max_length=10000)),
                ('firstlink', models.CharField(default=b'No Link Provided', max_length=40)),
                ('secondlink', models.CharField(default=b'No Link Provided', max_length=40)),
                ('thirdlink', models.CharField(default=b'No Link Provided', max_length=40)),
                ('count', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(to='Rebbit.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_rebb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_r', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to='Rebbit.Person')),
                ('votechoice', models.ForeignKey(to='Rebbit.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='subreddit',
            field=models.ForeignKey(to='Rebbit.Sub_rebb'),
        ),
        migrations.AddField(
            model_name='commentvoting',
            name='creator',
            field=models.ForeignKey(to='Rebbit.Person'),
        ),
        migrations.AddField(
            model_name='commentvoting',
            name='votechoice',
            field=models.ForeignKey(to='Rebbit.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(to='Rebbit.Person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='Rebbit.Post'),
        ),
    ]
