from django.db import models


class City(models.Model):
    """ Модель города
    """
    name = models.CharField(max_length=255, verbose_name='Название города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self) -> str:
        return self.name


class Citizen(models.Model):
    """ Модель жителя города
    """
    name = models.CharField(max_length=255, verbose_name='ФИО')
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             verbose_name='Город', related_name='citizen')

    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Жители'

    def __str__(self) -> str:
        return self.name
