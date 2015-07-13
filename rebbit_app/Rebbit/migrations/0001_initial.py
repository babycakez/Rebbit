# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('gender', models.IntegerField(choices=[(1, b'Male'), (2, b'Female')])),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rpost', models.CharField(max_length=500)),
                ('creator', models.ForeignKey(to='Rebbit.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_rebb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_r', models.CharField(max_length=20)),
                ('contributors', models.ForeignKey(to='Rebbit.Person')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sub_reb',
            field=models.ForeignKey(to='Rebbit.Sub_rebb'),
        ),
    ]
