import logging

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cinemaccs_project.models import Theater, Brand
from cinemaccs_project.serializers import (
    BrandSerializer,
    DescriptionElementSerializer,
    ExtraFieldMixin,
    TheaterPictureSerializer,
)

logger = logging.getLogger(__name__)


class TheaterSerializerNoRooms(
    ExtraFieldMixin,
    serializers.HyperlinkedModelSerializer
):

    full_name = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    accessibility_description = serializers.ReadOnlyField()

    brand_id = serializers.IntegerField(write_only=True)
    brand = BrandSerializer(read_only=True)

    pictures = TheaterPictureSerializer(many=True, read_only=True)
    description_elements = DescriptionElementSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = Theater
        fields = "__all__"
        extra_fields = ["id", "brand_id"]
        validators = [
            UniqueTogetherValidator(
                queryset=Theater.objects.all(),
                fields=["company_name", "internal_id"]
            )
        ]

    def create(self, validated_data):
        logger.error(
            "HEEEEEEEHOOOOOOOOOOOOO"
        )
        logger.error(
            validated_data
        )

        # brand
        brand_id = validated_data.pop('brand_id', -1)
        brand = validated_data.pop('brand', None)

        logger.error(
            brand_id,
            'TON PERE ----------------------------------------'
        )

        if brand_id == 0:
            if brand is not None:
                brand = Brand.objects.create(**brand)
        elif brand_id > 0:
            brand = Brand.objects.get(pk=brand_id)

        theater = Theater.objects.create(brand=brand, **validated_data)
        return theater


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
