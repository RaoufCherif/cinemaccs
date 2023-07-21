from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import (
    BrandSerializer, TheaterPictureSerializer,
    DescriptionElementSerializer, RoomSerializerNoTheater,
    ExtraFieldMixin
)


class TheaterSerializerNoRooms(
    ExtraFieldMixin, serializers.HyperlinkedModelSerializer
):
    full_name = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    accessibility_description = serializers.ReadOnlyField()

    brand = BrandSerializer(read_only=True)
    pictures = TheaterPictureSerializer(many=True, read_only=True)

    description_elements = DescriptionElementSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = Theater
        fields = '__all__'
        extra_fields = ['id']
        validators = [
            UniqueTogetherValidator(
                queryset=Theater.objects.all(),
                fields=['company_name', 'internal_id']
            )
        ]

    # For nested post
    # def create(self, validated_data):
    #     address_data = validated_data.pop('adresse')
    #     address = Adresse.objects.create(**address_data)
    #     organism = Organisme.objects.create(address=address, **validated_data)
    #     return organism 
    # Can be a special serializer for the put


class TheaterSerializer(TheaterSerializerNoRooms):
    rooms = RoomSerializerNoTheater(many=True, read_only=True)


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
