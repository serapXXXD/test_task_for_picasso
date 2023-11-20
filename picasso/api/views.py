from rest_framework.generics import ListAPIView, CreateAPIView
from .models import File
from .serializers import FileSerializer, UploadFileSerializer


class UploadViewSet(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = UploadFileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FileViewSet(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
