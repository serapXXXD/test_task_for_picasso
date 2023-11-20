from django.db import models


class File(models.Model):
    file = models.FileField()
    uploaded_at = models.DateField(auto_now_add=True, verbose_name='Дата загрузки')
    processed = models.BooleanField(verbose_name='Обработан')
