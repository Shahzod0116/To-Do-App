# Generated by Django 3.2.4 on 2021-08-03 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_todos_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
    ]
