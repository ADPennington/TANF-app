# Generated by Django 3.2.15 on 2023-09-14 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_indexes', '0025_tribal_tanf_t7'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tanf_t2',
            old_name='PARENT_WITH_MINOR_CHILD',
            new_name='PARENT_MINOR_CHILD',
        ),
    ]