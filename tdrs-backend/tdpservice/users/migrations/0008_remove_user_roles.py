# Generated by Django 3.1.4 on 2020-12-31 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201223_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
    ]
