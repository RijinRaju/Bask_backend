# Generated by Django 4.0.6 on 2022-12-25 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_alter_users_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisors', to=settings.AUTH_USER_MODEL)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.batch')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
