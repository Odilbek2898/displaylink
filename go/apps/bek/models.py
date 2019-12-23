import datetime
from django.db import models

from django.utils import timezone

class Registration(models.Model):
    registration_UserName = models.CharField('имя пользователья', max_length = 200)
    registration_UserPhone = models.IntegerField('номер пользователья')
    reg_date = models.DateTimeField('дата регистрации')

    def __str__(self):
        return self.registration_UserName

    def was_published_recently(self):
        return self.reg_date >= (timezone.now() - datetime.timedelta(days = 5))

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'