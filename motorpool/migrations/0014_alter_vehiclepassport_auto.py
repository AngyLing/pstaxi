# Generated by Django 3.2.4 on 2021-06-28 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0013_alter_auto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclepassport',
            name='auto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pts', to='motorpool.auto'),
        ),
    ]
