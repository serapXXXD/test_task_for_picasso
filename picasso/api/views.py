from rest_framework import viewsets
from models import File


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
