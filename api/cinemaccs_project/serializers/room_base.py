from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cinemaccs_project.models import Room
from cinemaccs_project.serializers import RoomPictureSerializer


class RoomSerializerBase(serializers.HyperlinkedModelSerializer):
    accessibility_description = serializers.ReadOnlyField()

    pictures = RoomPictureSerializer(many=True, read_only=True)

    # theater
    # description_elements

    class Meta:
        model = Room
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Room.objects.all(),
                fields=['theater', 'internal_room_id']
            )
        ]
