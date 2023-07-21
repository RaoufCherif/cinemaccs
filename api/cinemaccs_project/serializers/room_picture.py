from rest_framework import serializers

from cinemaccs_project.models import RoomPicture


class RoomPictureSerializer(serializers.HyperlinkedModelSerializer):
    photo_ext_url = serializers.SerializerMethodField()

    class Meta:
        model = RoomPicture
        fields = ('id', 'room_id', 'legend', 'photo_ext_url')

    def get_photo_ext_url(self, room_picture):
        request = self.context.get('request')
        photo_url = room_picture.photo.url
        return request.build_absolute_uri(photo_url)
