# Generated by Django 5.0 on 2023-12-12 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='finch',
        ),
    ]
