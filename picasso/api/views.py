from rest_framework.generics import ListAPIView, CreateAPIView
from .models import File
from .serializers import FileSerializer
from .tasks import celery_file_worker
import magic

mime = magic.Magic(mime=True)


class UploadCreateView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        new_file = serializer.save()
        celery_file_worker.delay(new_file.id)


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
