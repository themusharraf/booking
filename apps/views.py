from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.models import Room
from apps.serializers import RoomModelSerializer, BookModelSerializer
from apps.services import get_free_time


class RoomReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer

    @action(['GET'], detail=True)
    def availability(self, request, pk):
        response = get_free_time(request, pk)
        return Response(response)

    @action(['POST'], detail=True, serializer_class=BookModelSerializer)
    def book(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(room_id=pk)
            response = {
                "message": "xona muvaffaqiyatli band qilindi"
            }
            return Response(response, status.HTTP_201_CREATED)
        response = {
            "error": "uzr, siz tanlagan vaqtda xona band"
        }
        return Response(response, status.HTTP_410_GONE)
