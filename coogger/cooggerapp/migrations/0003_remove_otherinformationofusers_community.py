# Generated by Django 2.0 on 2018-07-07 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0002_auto_20180708_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherinformationofusers',
            name='community',
        ),
    ]