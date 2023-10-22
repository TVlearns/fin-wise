# Generated by Django 4.2.4 on 2023-10-03 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bills", "0004_alter_bill_recurring"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bills",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
