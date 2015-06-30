# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(verbose_name=b'tipo', choices=[(1, b'video')])),
                ('path', models.CharField(help_text=b'a partire dalla directory media/attachment/TYPE', max_length=255, verbose_name=b'percorso')),
                ('notes', models.TextField(verbose_name=b'note')),
            ],
            options={
                'verbose_name': 'Allegato',
                'verbose_name_plural': 'Allegati',
            },
        ),
    ]
