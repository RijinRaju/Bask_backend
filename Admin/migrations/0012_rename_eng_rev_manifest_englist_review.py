# Generated by Django 4.0.6 on 2023-01-03 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_rename_extra_workout_manifest_extra_workouts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manifest',
            old_name='eng_rev',
            new_name='englist_review',
        ),
    ]