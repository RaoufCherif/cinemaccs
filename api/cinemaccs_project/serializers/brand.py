from rest_framework import serializers

from cinemaccs_project.models import Brand
from cinemaccs_project.serializers import ExtraFieldMixin


class BrandSerializer(
    ExtraFieldMixin, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = Brand
        fields = "__all__"
        extra_fields = ["id"]
