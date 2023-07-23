from rest_framework import serializers

from cinemaccs_project.models import TheaterPicture


class TheaterPictureSerializer(serializers.HyperlinkedModelSerializer):
    photo_ext_url = serializers.SerializerMethodField()

    class Meta:
        model = TheaterPicture
        fields = "__all__"

    def get_photo_ext_url(self, theater_picture):
        request = self.context.get("request")
        photo_url = theater_picture.photo.url
        return request.build_absolute_uri(photo_url)
