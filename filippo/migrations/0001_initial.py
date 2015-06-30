# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'data')),
                ('title', models.CharField(max_length=128, verbose_name=b'titolo')),
                ('text', ckeditor.fields.RichTextField(verbose_name=b'testo')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Pagine',
            },
        ),
    ]
