# Generated by Django 4.2.4 on 2023-09-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("estetica", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agendamento",
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
                ("data_hora", models.DateField(blank=True, null=True)),
                ("confirmacao", models.CharField(max_length=100)),
                (
                    "Cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Agendamento",
                        to="estetica.cliente",
                    ),
                ),
                (
                    "Procedimento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Agendamento",
                        to="estetica.procedimento",
                    ),
                ),
            ],
        ),
    ]
