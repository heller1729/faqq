# Generated by Django 3.0.5 on 2020-04-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_destination_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
