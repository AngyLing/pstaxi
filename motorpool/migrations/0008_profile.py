# Generated by Django 3.2.4 on 2021-06-26 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('motorpool', '0007_vehiclepassport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]