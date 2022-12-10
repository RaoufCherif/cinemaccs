from rest_framework import viewsets
from cinemaccs_project.serializers import TheaterSerializer
from cinemaccs_project.models import Theater


class TheaterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
