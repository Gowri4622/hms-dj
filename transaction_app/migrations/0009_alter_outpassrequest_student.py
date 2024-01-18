# Generated by Django 5.0.1 on 2024-01-17 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("master_app", "0009_alter_room_room_number_alter_room_student"),
        ("transaction_app", "0008_alter_outpassrequest_warden"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outpassrequest",
            name="student",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="master_app.student",
            ),
        ),
    ]