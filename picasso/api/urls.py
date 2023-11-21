from .views import UploadCreateView, FileListView
from django.urls import path

urlpatterns = [
    path('upload/', UploadCreateView.as_view()),
    path('files/', FileListView.as_view()),
              ]
