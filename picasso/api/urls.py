from rest_framework import routers
from .views import FileViewSet, UploadViewSet
from django.urls import path

app_name = 'api'

# router = routers.SimpleRouter()
#
# router.register('upload/', UploadViewSet)
# router.register('file/', FileViewSet)

urlpatterns = [
    path('upload/', UploadViewSet.as_view()),
    path('file/', FileViewSet.as_view()),
              ]
