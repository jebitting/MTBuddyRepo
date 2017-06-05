# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='traveling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='userMTB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=200)),
                ('hashpass', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtbuddy.userMTB'),
        ),
        migrations.AddField(
            model_name='traveling',
            name='traveling_trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtbuddy.trip'),
        ),
        migrations.AddField(
            model_name='traveling',
            name='traveling_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtbuddy.userMTB'),
        ),
    ]
