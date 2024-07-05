from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .api.viewsets import NewsViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
