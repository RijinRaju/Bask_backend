# Generated by Django 4.0.6 on 2023-01-02 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_alter_manifest_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manifest',
            old_name='Extra_workout',
            new_name='extra_workouts',
        ),
        migrations.RenameField(
            model_name='manifest',
            old_name='Total',
            new_name='total',
        ),
        migrations.RenameField(
            model_name='manifest',
            old_name='task',
            new_name='week_task',
        ),
    ]
