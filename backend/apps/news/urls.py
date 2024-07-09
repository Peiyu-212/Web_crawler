from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from .api.consumer import NewsConsumer
from .api.viewsets import NewsViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]

socket_urlpatterns = [
    re_path(r'news/', NewsConsumer.as_asgi()),
]
