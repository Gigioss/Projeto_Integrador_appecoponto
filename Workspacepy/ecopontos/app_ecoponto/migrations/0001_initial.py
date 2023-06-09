# Generated by Django 4.1.7 on 2023-04-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classes",
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
                ("numero", models.CharField(default="-", max_length=15)),
                ("CEP", models.CharField(default="-", max_length=15)),
                ("BAIRRO", models.CharField(default="-", max_length=10)),
                ("ENDERECO", models.CharField(default="-", max_length=15)),
                ("SITUACAO", models.CharField(default="-", max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("ENDERECO", models.CharField(default="-", max_length=15)),
                ("funcao", models.CharField(default="-", max_length=15)),
            ],
        ),
    ]
