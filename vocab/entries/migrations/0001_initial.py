# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 17:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=256)),
                ('definition', models.TextField(null=True)),
                ('definition_source', models.CharField(max_length=256, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]