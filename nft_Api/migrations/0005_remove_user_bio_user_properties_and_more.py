# Generated by Django 4.0.3 on 2022-03-17 15:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft_Api', '0004_rename_properties_user_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.AddField(
            model_name='user',
            name='properties',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='collection',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='offers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
    ]
