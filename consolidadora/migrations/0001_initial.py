# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:41
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
            name='Consolidadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.BooleanField(default=True)),
                ('telefono1', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('imagen', models.ImageField(blank=True, default='images/default.png', null=True, upload_to='imagnes/consolidadora', verbose_name='Imagen Consolidadora')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]