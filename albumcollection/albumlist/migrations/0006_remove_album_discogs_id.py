# Generated by Django 2.1.4 on 2018-12-06 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumlist', '0005_album_discogs_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='discogs_id',
        ),
    ]