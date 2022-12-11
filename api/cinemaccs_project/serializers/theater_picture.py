from rest_framework import serializers

from cinemaccs_project.models import TheaterPictures
from cinemaccs_project.serializers import theater_picture


class TheaterPictureSerializer(serializers.ModelSerializer):
    XXX