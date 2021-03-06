# Generated by Django 2.1.4 on 2018-12-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumlist', '0002_auto_20181204_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='location',
            field=models.IntegerField(choices=[(1, 'shelf'), (2, 'harddrive'), (3, 'bandcamp')], default=1),
        ),
        migrations.AlterField(
            model_name='album',
            name='type',
            field=models.IntegerField(choices=[(1, 'LP'), (2, 'CD'), (3, 'tape'), (4, 'file')], default=1),
        ),
    ]
