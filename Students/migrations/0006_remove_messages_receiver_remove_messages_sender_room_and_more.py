# Generated by Django 4.0.6 on 2023-01-08 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Students', '0005_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='sender',
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=150, null=True)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='messages',
            name='room_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Students.room'),
        ),
    ]