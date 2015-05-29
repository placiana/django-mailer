# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DontSendEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_address', models.EmailField(max_length=75)),
                ('when_added', models.DateTimeField()),
            ],
            options={
                'verbose_name': "don't send entry",
                'verbose_name_plural': "don't send entries",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_data', models.TextField()),
                ('when_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.CharField(default=b'2', max_length=1, choices=[(b'1', b'high'), (b'2', b'medium'), (b'3', b'low'), (b'4', b'deferred')])),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_data', models.TextField()),
                ('when_added', models.DateTimeField(db_index=True)),
                ('priority', models.CharField(db_index=True, max_length=1, choices=[(b'1', b'high'), (b'2', b'medium'), (b'3', b'low'), (b'4', b'deferred')])),
                ('when_attempted', models.DateTimeField(default=django.utils.timezone.now)),
                ('result', models.CharField(max_length=1, choices=[(b'1', b'success'), (b'2', b"don't send"), (b'3', b'failure')])),
                ('log_message', models.TextField()),
            ],
            options={
                'verbose_name': 'message log',
                'verbose_name_plural': 'message logs',
            },
            bases=(models.Model,),
        ),
    ]
