# Generated by Django 5.0.1 on 2024-01-17 03:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("master_app", "0007_remove_room_hostel_remove_student_room_assets_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="Student",
            new_name="student",
        ),
    ]
