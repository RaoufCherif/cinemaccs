from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cinemaccs_project.models import Room
from cinemaccs_project.serializers import (
    RoomPictureSerializer, DescriptionElementSerializer,
    TheaterSerializerNoRooms
)


class RoomSerializerNoTheater(serializers.HyperlinkedModelSerializer):
    accessibility_description = serializers.ReadOnlyField()

    pictures = RoomPictureSerializer(many=True, read_only=True)

    description_elements = DescriptionElementSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = Room
        fields = '__all__'
        extra_fields = ['id']
        validators = [
            UniqueTogetherValidator(
                queryset=Room.objects.all(),
                fields=['company_name', 'internal_id']
            )
        ]


class RoomSerializer(RoomSerializerNoTheater):
    theater = TheaterSerializerNoRooms(read_only=True)
