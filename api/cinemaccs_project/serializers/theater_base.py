from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cinemaccs_project.models import Theater
from cinemaccs_project.serializers import TheaterPictureSerializer


class TheaterSerializerBase(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    accessibility_description = serializers.ReadOnlyField()

    pictures = TheaterPictureSerializer(many=True, read_only=True)

    # brand
    # description_elements

    class Meta:
        model = Theater
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Theater.objects.all(),
                fields=["company_name", "internal_id"]
            )
        ]


class TheaterSerializerList(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Theater
        fields = [
            "url",
            "full_name",
            "address",
            "zipcode",
        ]
