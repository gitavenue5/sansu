# Generated by Django 3.1 on 2020-08-12 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family_site', '0015_auto_20180310_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notecomment',
            name='note',
        ),
        migrations.RemoveField(
            model_name='notecomment',
            name='notecomment_author',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='NoteComment',
        ),
    ]
