# Generated by Django 3.2.15 on 2024-02-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_indexes', '0026_parent_minor_child_rename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanf_t2',
            name='DATE_OF_BIRTH',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='tanf_t3',
            name='DATE_OF_BIRTH',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='tribal_tanf_t2',
            name='DATE_OF_BIRTH',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='tribal_tanf_t3',
            name='DATE_OF_BIRTH',
            field=models.CharField(max_length=8, null=True),
        ),
    ]