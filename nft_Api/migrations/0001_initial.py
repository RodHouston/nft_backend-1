# Generated by Django 4.0.3 on 2022-03-17 15:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(default='none')),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('offer', models.BooleanField(default=False)),
                ('properties', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(default='none')),
                ('fname', models.CharField(max_length=32)),
                ('lname', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=50)),
                ('collection', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('properties', models.TextField()),
            ],
        ),
    ]
