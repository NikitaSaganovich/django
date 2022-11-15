from django.db import models

class Task(models.model):
    title = models.Charfield('Название', max_length = 50)
    task = models.textField('Описание')
    date = models.Charfield('Дата изменения', max_length = 20)
    name = models.Charfield('Имя редактора', max_length = 30)

    def __str__(self):
        return self.Title