# Generated by Django 5.0.4 on 2024-04-09 10:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_clients_rename_integer_payments_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clients",
            old_name="joining_data",
            new_name="joining_date",
        ),
    ]
