from django.db import models

# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=104, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Бренды'
        verbose_name = 'Бренд'

    def __str__(self):
        return self.title


class Option(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Опции'

    def __str__(self):
        return self.title


class Auto(models.Model):
    AUTO_CLASS_ECONOMY = 'e'
    AUTO_CLASS_COMFORT = 'c'
    AUTO_CLASS_BUSINESS = 'b'

    AUTO_CLASS_CHOICES = (
        (AUTO_CLASS_ECONOMY, 'economy'),
        (AUTO_CLASS_COMFORT, 'comfort'),
        (AUTO_CLASS_BUSINESS, 'business'),
    )
    number = models.CharField(max_length=15)
    description = models.TextField(max_length=500, default='', blank=True)
    year = models.PositiveSmallIntegerField(null=True)
    auto_class = models.CharField(max_length=1, null=True, choices=AUTO_CLASS_CHOICES, default=AUTO_CLASS_ECONOMY)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'


class VehiclePassport(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE)
    vin = models.CharField(max_length=30, verbose_name='Идентификационный номер (VIN)')
    engine_volume = models.SmallIntegerField(verbose_name='Объем двигателя, куб.см')
    engine_power = models.SmallIntegerField(verbose_name='Мощность двигателя, л.с.')

    def __str__(self):
        return f'{self.auto}::{self.vin}'

    class Meta:
        verbose_name_plural = 'Паспорта машин'
        verbose_name = 'Паспорт машины'


from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='О себе')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=250, null=True, blank=True, verbose_name='Адрес')
