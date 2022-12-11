from rest_framework import viewsets

from cinemaccs_project.serializers import (
    TheaterListSerializer, TheaterSerializer
)
from cinemaccs_project.models import Theater


class TheaterViewset(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Theater.objects.all()

    default_serializer = TheaterSerializer

    custom_serializer = {
        'list': TheaterListSerializer,
    }

    def get_serializer_class(self):
        return self.custom_serializer.get(
            self.action, self.default_serializer
        )
