# Generated by Django 4.1.7 on 2023-04-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_ecoponto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Descartadores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(default="-", max_length=15)),
                ("cpf", models.CharField(default="-", max_length=15)),
                ("email", models.CharField(default="-", max_length=10)),
            ],
        ),
    ]
