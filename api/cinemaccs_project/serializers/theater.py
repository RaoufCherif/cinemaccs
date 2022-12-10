from rest_framework import serializers

from cinemaccs_project.models import Theater


class TheaterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theater
        fields = [
            "name",
            "zipcode"
        ]


class TheaterRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        # TODO
        model = Theater
        fields = ["name", "zipcode"]
