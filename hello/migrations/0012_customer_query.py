# Generated by Django 3.0.5 on 2020-04-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0011_campaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
