# Generated by Django 5.0.4 on 2024-05-05 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Todo',
        ),
    ]