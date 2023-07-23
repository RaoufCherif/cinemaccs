from rest_framework import permissions, viewsets

from cinemaccs_project.models import DescriptionElement
from cinemaccs_project.serializers import DescriptionElementSerializer


class DescriptionElementViewSet(viewsets.ModelViewSet):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = DescriptionElement.objects.all()
    serializer_class = DescriptionElementSerializer
