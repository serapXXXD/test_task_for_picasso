from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки')
    processed = models.BooleanField(verbose_name='Обработан', default=False)

    def __str__(self):
        return f'{self.file.name}, {self.uploaded_at}, {self.processed}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
