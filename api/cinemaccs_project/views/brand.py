from cinemaccs_project.models import Brand
from cinemaccs_project.serializers import BrandSerializer
from rest_framework import permissions, viewsets


class BrandViewSet(viewsets.ModelViewSet):
    """
    The theater viewset that give a lightweight
    json when list is asked.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
