from rest_framework import permissions, viewsets

from cinemaccs_project.models import TheaterPicture
from cinemaccs_project.serializers import TheaterPictureSerializer


class TheaterPictureViewSet(viewsets.ModelViewSet):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = TheaterPicture.objects.all()
    serializer_class = TheaterPictureSerializer
