from picasso.celery import app
from .models import File


@app.task
def celery_file_worker(file_id):
    file_obj = File.objects.get(id=file_id)
    with open(file_obj.file.path, 'r') as read_file:
        print(f"Обработака файла {file_obj.file.name}")
    if not file_obj.processed:
        file_obj.processed = True
        file_obj.save()
