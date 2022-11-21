from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    task = models.TextField('Описание')
    date = models.CharField('Дата изменения', max_length=20)
    name = models.CharField('Имя редактора', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"

