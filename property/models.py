from tkinter.constants import CASCADE

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Complaints(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='complaints', verbose_name="Кто пожаловался")
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, related_name='complaints', verbose_name='Квартира, на которую пожаловались')
    complaints = models.TextField(verbose_name='Жалоба')


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    owner_pure_phone = PhoneNumberField(verbose_name="Номер владельца", blank=True, null=True)
    flat = models.ManyToManyField('Flat', blank=True, related_name='owners', verbose_name='Квартиры в собственности')

    def __str__(self):
        return f'{self.name}'

class Flat(models.Model):
    new_building = models.BooleanField(null=True, db_index=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)

    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(User, blank=True, related_name='liked_flats', verbose_name="Кто лайкнул")

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


