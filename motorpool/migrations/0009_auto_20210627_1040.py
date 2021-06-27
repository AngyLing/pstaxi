# Generated by Django 3.2.4 on 2021-06-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0008_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='vehiclepassport',
            options={'verbose_name_plural': 'Паспорта машин'},
        ),
        migrations.AlterField(
            model_name='auto',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='auto',
            name='year',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
