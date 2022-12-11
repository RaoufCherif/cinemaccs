from rest_framework import serializers

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import TheaterPictureSerializer


class TheaterSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.Field()
    address = serializers.Field()
    pictures = TheaterPictureSerializer(many=True)

    # TODO: Render logo url
    # TODO: Render description rendering
    # TODO
    # # room_set
    # # rooms

    class Meta:
        model = Theater
        fields = "__all__"


class TheaterListSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.Field()

    class Meta:
        model = Theater
        fields = [
            "full_name",
            "address",
            "zipcode",
        ]
