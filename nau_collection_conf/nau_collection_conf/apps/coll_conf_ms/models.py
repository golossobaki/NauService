import datetime
from django.db import models
from django.utils import timezone


class Service(models.Model):
    Name = models.CharField('Название сервиса', max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Config(models.Model):
    ServiceId = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Сервис')
    FileName = models.CharField('Имя файла', max_length=50)
    Host = models.CharField('IP адрес', max_length=15)
    Path = models.CharField('Путь до файла', max_length=50)

    def __str__(self):
        return self.FileName

    class Meta:
        verbose_name = 'Конфиг'
        verbose_name_plural = 'Кофиги'


class ConfigHistory(models.Model):
    ConfigId = models.ForeignKey(Config, on_delete=models.CASCADE, verbose_name='Конфиг')
    Text = models.TextField('Содержание файла')
    LastModified = models.DateTimeField('Последнее изенение файла', auto_now_add=True)

    def __str__(self):
        return self.ConfigId

    def was_last_modified(self):
        return self.LastModified >= (timezone.now() - datetime.timedelta(hours=1))

    class Meta:
        verbose_name = 'История конфигов'
        verbose_name_plural = 'Истории конфигов'
