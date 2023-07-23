from rest_framework import permissions, viewsets

from cinemaccs_project.models import RoomPicture
from cinemaccs_project.serializers import RoomPictureSerializer


class RoomPictureViewSet(viewsets.ModelViewSet):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = RoomPicture.objects.all()
    serializer_class = RoomPictureSerializer
