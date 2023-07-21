from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import (
    BrandSerializer,
    DescriptionElementSerializer,
    ExtraFieldMixin,
    TheaterPictureSerializer,
)
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class TheaterSerializer(ExtraFieldMixin, serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    pictures = TheaterPictureSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    description_elements = DescriptionElementSerializer(read_only=True, many=True)

    # TODO: Render description rendering
    # TODO
    # # room_set
    # # rooms

    class Meta:
        model = Theater
        fields = "__all__"
        extra_fields = ["id"]
        validators = [
            UniqueTogetherValidator(
                queryset=Theater.objects.all(), fields=["company_name", "internal_id"]
            )
        ]


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
