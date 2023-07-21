from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import TheaterListSerializer, TheaterSerializer
from rest_framework import permissions, viewsets


class TheaterViewSet(viewsets.ModelViewSet):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Theater.objects.all()

    default_serializer = TheaterSerializer
    custom_serializer = {
        "list": TheaterListSerializer,
    }

    def get_serializer_class(self):
        return self.custom_serializer.get(self.action, self.default_serializer)
