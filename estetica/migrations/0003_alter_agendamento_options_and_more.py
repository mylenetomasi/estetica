# Generated by Django 4.2.4 on 2023-09-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estetica", "0002_agendamento"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agendamento",
            options={"verbose_name_plural": "Agendamentos"},
        ),
        migrations.RenameField(
            model_name="agendamento",
            old_name="Cliente",
            new_name="cliente",
        ),
        migrations.RenameField(
            model_name="agendamento",
            old_name="Procedimento",
            new_name="procedimento",
        ),
        migrations.AddField(
            model_name="agendamento",
            name="nome",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
