# Generated by Django 5.0.1 on 2024-01-18 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("master_app", "0010_alter_room_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parent",
            name="child",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="master_app.student",
            ),
        ),
    ]
