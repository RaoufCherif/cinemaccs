from rest_framework import permissions
from rest_framework import viewsets

from cinemaccs_project.models import Room
from cinemaccs_project.serializers import (
    RoomSerializerBase,
    RoomSerializerGet
)
from cinemaccs_project.views import (
    DefaultCustomMixin,
    BatchCreateMixin
)


class RoomViewSet(
    BatchCreateMixin,
    DefaultCustomMixin,
    viewsets.ModelViewSet
):
    """
    The Room viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Room.objects.all()

    default_serializer = RoomSerializerBase
    custom_serializer = {
        "retrieve": RoomSerializerGet,
    }
