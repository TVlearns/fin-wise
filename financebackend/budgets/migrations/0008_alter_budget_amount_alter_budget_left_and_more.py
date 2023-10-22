# Generated by Django 4.2.4 on 2023-09-26 01:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0007_alter_budget_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="budget",
            name="amount",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="budget",
            name="left",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="budget",
            name="spent",
            field=models.IntegerField(default=0),
        ),
    ]
