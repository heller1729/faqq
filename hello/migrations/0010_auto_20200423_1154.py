# Generated by Django 3.0.5 on 2020-04-23 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20200423_1150'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
