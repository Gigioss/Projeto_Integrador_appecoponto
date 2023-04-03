# Generated by Django 4.1.7 on 2023-04-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_ecoponto", "0003_descartadores_endereco"),
    ]

    operations = [
        migrations.CreateModel(
            name="Descarte",
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
                ("Ultimo_descarte", models.CharField(default="-", max_length=10)),
                ("Proximo_descarte", models.CharField(default="-", max_length=15)),
            ],
        ),
    ]