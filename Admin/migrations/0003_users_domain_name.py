# Generated by Django 4.0.6 on 2022-12-18 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_alter_users_batch_alter_users_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='domain_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.domain'),
        ),
    ]
