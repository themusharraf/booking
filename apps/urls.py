from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import RoomReadOnlyModelViewSet

router = DefaultRouter(trailing_slash=False)
router.register('rooms', RoomReadOnlyModelViewSet, 'room')

urlpatterns = [
    path('', include(router.urls))
]
