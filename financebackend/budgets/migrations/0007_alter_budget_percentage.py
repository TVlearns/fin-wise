# Generated by Django 4.2.4 on 2023-09-25 02:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0006_budget_left_budget_percentage_budget_spent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="budget",
            name="percentage",
            field=models.IntegerField(default=0),
        ),
    ]
