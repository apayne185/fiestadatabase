# Generated by Django 4.1.13 on 2023-12-02 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clubbing", "0004_remove_event_club_event_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="clubbing.city",
            ),
        ),
    ]