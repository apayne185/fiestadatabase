# Generated by Django 4.1.13 on 2023-12-02 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clubbing", "0003_alter_review_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="club",
        ),
        migrations.AddField(
            model_name="event",
            name="city",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="clubbing.city",
            ),
        ),
    ]
