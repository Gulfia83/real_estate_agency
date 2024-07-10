from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца',
                                        blank=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    new_building = models.BooleanField('Является новостройкой',
                                       default=False, blank=True)
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

    has_balcony = models.BooleanField('Наличие балкона',
                                      db_index=True,
                                      default=False)
    active = models.BooleanField('Активно-ли объявление',
                                 db_index=True,
                                 default=False)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    liked_by = models.ManyToManyField(User,
                                      verbose_name='Кто лайкнул',
                                      related_name='liked_flats',
                                      blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'
    

class Claim(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Кто пожаловался',
                             related_name='user_claims')
    flat = models.ForeignKey(Flat,
                             on_delete=models.CASCADE,
                             verbose_name='Квартира, на которую пожаловались',
                             related_name='claims')
    text = models.TextField(verbose_name='Текст жалобы')

    def __str__(self):
        return f'От {self.user.username} на {self.flat.address}'
