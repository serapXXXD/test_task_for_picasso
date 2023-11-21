from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ('processed',)

    def get_file_name(self, obj):
        return obj.file.name.split('/')[-1]
