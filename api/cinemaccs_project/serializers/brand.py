from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cinemaccs_project.models import Brand


class BrandSerializer(
    serializers.HyperlinkedModelSerializer
):
    logo_ext_url = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Brand.objects.all(),
                fields=['company_name']
            )
        ]

    def get_logo_ext_url(self, brand):
        request = self.context.get("request")
        logo_url = brand.logo.url
        return request.build_absolute_uri(logo_url)
