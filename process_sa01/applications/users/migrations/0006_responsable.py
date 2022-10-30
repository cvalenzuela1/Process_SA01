# Generated by Django 4.1 on 2022-10-30 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_delete_permisos"),
    ]

    operations = [
        migrations.CreateModel(
            name="Responsable",
            fields=[
                (
                    "persona_id_persona",
                    models.OneToOneField(
                        db_column="persona_id_persona",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="users.persona",
                    ),
                ),
                ("fecha_generacion", models.DateField()),
            ],
            options={"db_table": "responsable", "managed": False,},
        ),
    ]