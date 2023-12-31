# Generated by Django 4.2.7 on 2023-11-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки')),
                ('processed', models.BooleanField(verbose_name='Обработан')),
            ],
        ),
    ]
