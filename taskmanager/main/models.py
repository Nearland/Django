from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=25)
    task = models.TextField('Задача', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
