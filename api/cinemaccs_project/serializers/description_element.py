from cinemaccs_project.models import DescriptionElement
from rest_framework import serializers


class DescriptionElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DescriptionElement
        fields = "__all__"
