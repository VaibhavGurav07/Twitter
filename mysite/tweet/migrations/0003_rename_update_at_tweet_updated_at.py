# Generated by Django 5.1.1 on 2024-10-15 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_rename_updated_at_tweet_update_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
