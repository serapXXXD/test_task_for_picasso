from rest_framework import routers
from views import FileViewSet

app_name = 'api'

router = routers.SimpleRouter()

router.register('files', FileViewSet)

urlpatterns = [] + router.urls
