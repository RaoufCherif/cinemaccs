from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import (
    TheaterListSerializer,
    TheaterSerializer,
)
from cinemaccs_project.views import DefaultCustomMixin


class TheaterViewSet(DefaultCustomMixin, viewsets.ModelViewSet):
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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(
    #         data=request.data,
    #         many=isinstance(request.data, list)
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(
    #         serializer.data,
    #         status=status.HTTP_201_CREATED,
    #         headers=headers
    #     )
