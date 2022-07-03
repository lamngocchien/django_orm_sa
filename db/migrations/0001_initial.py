# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ac_reg', models.CharField(max_length=64, default='')),
                ('type', models.CharField(max_length=64, default='')),
                ('arr', models.CharField(max_length=64, default='')),
                ('dep', models.CharField(max_length=64, default='')),
                ('route', models.CharField(max_length=64, default='')),
                ('date', models.DateField(blank=True, null=True)),
                ('eta', models.DateTimeField(blank=True, null=True)),
                ('etd', models.DateTimeField(blank=True, null=True)),
                ('time_eta', models.CharField(max_length=64, default='')),
                ('time_etd', models.CharField(max_length=64, default='')),
                ('enable', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Record',
            },
        ),
    ]
