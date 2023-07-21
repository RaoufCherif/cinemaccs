from rest_framework import permissions
from rest_framework import viewsets

from cinemaccs_project.models import Room
from cinemaccs_project.serializers import (
    RoomSerializer, DefaultCustomMixin
)


class RoomViewSet(DefaultCustomMixin, viewsets.ModelViewSet):
    """
    The Room viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Room.objects.all()

    default_serializer = RoomSerializer
