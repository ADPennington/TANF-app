# Generated by Django 3.1.1 on 2020-12-14 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

options={
    "db_table": 'reports_reportfile'
}

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stts", "0002_auto_20200923_1809"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    replaces = [('reports','0001_initial')]

    operations = [
        migrations.CreateModel(
            name="DataFile",
            options=options,
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_filename", models.CharField(max_length=256)),
                ("slug", models.CharField(max_length=256, unique=True)),
                ("extension", models.CharField(default="txt", max_length=8)),
                (
                    "quarter",
                    models.CharField(
                        choices=[
                            ("Q1", "Q1"),
                            ("Q2", "Q2"),
                            ("Q3", "Q3"),
                            ("Q4", "Q4"),
                        ],
                        max_length=16,
                    ),
                ),
                ("year", models.CharField(max_length=16)),
                (
                    "section",
                    models.CharField(
                        choices=[
                            ("Active Case Data", "Active Case Data"),
                            ("Close Case Data", "Close Case Data"),
                            ("Aggregate Data", "Aggregate Data"),
                            ("Stratum Data", "Stratum Data"),
                        ],
                        max_length=32,
                    ),
                ),
                ("version", models.IntegerField()),
                (
                    "stt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sttRef",
                        to="stts.stt",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="datafile",
            constraint=models.UniqueConstraint(
                fields=("section", "version", "quarter", "year", "stt"),
                name="constraint_name",
            ),
        ),
    ]
