from rest_framework import serializers

from cinemaccs_project.models import DescriptionElement


class DescriptionElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DescriptionElement
        fields = "__all__"
