# Generated by Django 4.2.4 on 2023-08-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bills", "0002_alter_bill_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="isPaid",
            field=models.BooleanField(default=False),
        ),
    ]
