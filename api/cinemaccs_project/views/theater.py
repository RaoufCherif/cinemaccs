from rest_framework import permissions, viewsets

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import (
    TheaterSerializerBase,
    TheaterSerializerList,
    TheaterSerializerGet
)
from cinemaccs_project.views import (
    DefaultCustomMixin,
    BatchCreateMixin
)


class TheaterViewSet(
    BatchCreateMixin,
    DefaultCustomMixin,
    viewsets.ModelViewSet
):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Theater.objects.all()

    default_serializer = TheaterSerializerBase
    custom_serializer = {
        "list": TheaterSerializerList,
        "retrieve": TheaterSerializerGet,
    }
