# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Configuration name')),
                ('email', models.EmailField(max_length=75)),
                ('host', models.CharField(max_length=100, verbose_name=b'Host')),
                ('port', models.IntegerField(verbose_name=b'Port')),
                ('username', models.CharField(max_length=100, verbose_name=b'Username')),
                ('password', models.CharField(max_length=100, verbose_name=b'Password')),
                ('use_tls', models.BooleanField(default=False, verbose_name=b'Enable TLS')),
                ('is_default', models.BooleanField(default=False, verbose_name=b'Is default configuration')),
            ],
            options={
                'verbose_name': 'outgoing email configuration',
                'verbose_name_plural': 'outgoing email configurations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='configuration',
            field=models.ForeignKey(blank=True, to='mailer.EmailConfiguration', null=True),
            preserve_default=True,
        ),
    ]
