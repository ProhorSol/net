from django.db import models

class Task(models.Model):
    num = models.CharField("Номер автомобиля", max_length=9)
    opisanie = models.TextField('Описание нарушения')
    stat = (('рассматривается','рассматривается'),('отклонено','отклонено'))
    status = models.CharField('Статус', max_length=100, choices=stat, default="")

    def __str__(self):
        return self.num

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
