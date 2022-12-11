from rest_framework import serializers

from cinemaccs_project.models import Brand


class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'
