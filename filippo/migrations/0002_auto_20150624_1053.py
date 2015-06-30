# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filippo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('-date',), 'verbose_name': 'Pagina', 'verbose_name_plural': 'Pagine'},
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name=b'slug'),
            preserve_default=False,
        ),
    ]
