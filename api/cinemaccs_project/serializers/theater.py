from cinemaccs_project.models import Theater
from rest_framework import serializers


class TheaterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theater
        fields = ["name", "zipcode"]
