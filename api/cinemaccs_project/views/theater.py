from rest_framework import viewsets

from cinemaccs_project.serializers import (
    TheaterListSerializer, TheaterRetrieveSerializer
)
from cinemaccs_project.models import Theater


class TheaterViewset(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Theater.objects.all()

    serializer_classes = {
        'list': TheaterListSerializer,
        'retrieve': TheaterRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]
