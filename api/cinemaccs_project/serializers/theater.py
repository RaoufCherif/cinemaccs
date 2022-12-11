from rest_framework import serializers

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import TheaterPictureSerializer


class TheaterSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.Field(read_only=True)
    address = serializers.Field(read_only=True)
    pictures = TheaterPictureSerializer(many=True)
    # Render accessibility text

    class Meta:
        model = Theater
        fields = "__all__"


class TheaterListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Theater
        fields = [
            "full_name",
            "address",
            "zipcode",
            "logo"
        ]
