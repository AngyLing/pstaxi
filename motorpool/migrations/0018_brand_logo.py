# Generated by Django 3.2.4 on 2021-07-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0017_alter_vehiclepassport_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='motorpool/brands/'),
        ),
    ]
