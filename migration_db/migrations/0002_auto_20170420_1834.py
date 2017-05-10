# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migration_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='File')),
                ('name', models.CharField(max_length=50, verbose_name='filename')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_id',
            new_name='index_id',
        ),
        migrations.AddField(
            model_name='project',
            name='Project',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='node',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_define1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_define2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
