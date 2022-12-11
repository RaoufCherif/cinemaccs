from rest_framework import serializers

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import (
    TheaterPictureSerializer, DescriptionElementSerializer
)


class TheaterSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    pictures = TheaterPictureSerializer(many=True, read_only=True)
    description_elements = DescriptionElementSerializer(
        read_only=True, many=True
    )

    # TODO: Render logo url
    # TODO: Render description rendering
    # TODO
    # # room_set
    # # rooms

    class Meta:
        model = Theater
        fields = "__all__"


class TheaterListSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Theater
        fields = [
            "id",
            "full_name",
            "address",
            "zipcode",
        ]
