from cinemaccs_project.models import Brand
from rest_framework import serializers


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
