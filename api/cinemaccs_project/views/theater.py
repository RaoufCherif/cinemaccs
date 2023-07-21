from rest_framework import permissions
from rest_framework import viewsets

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import (
    TheaterListSerializer, TheaterSerializer, DefaultCustomMixin
)


class TheaterViewSet(DefaultCustomMixin, viewsets.ModelViewSet):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Theater.objects.all()

    default_serializer = TheaterSerializer
    custom_serializer = {
        'list': TheaterListSerializer,
    }
