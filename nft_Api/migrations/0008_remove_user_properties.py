# Generated by Django 4.0.3 on 2022-03-17 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nft_Api', '0007_alter_user_collection_alter_user_offers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='properties',
        ),
    ]
