# Generated by Django 2.2.13 on 2020-07-14 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200714_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='datadog_api_base_url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='datadog_api_key',
        ),
    ]
