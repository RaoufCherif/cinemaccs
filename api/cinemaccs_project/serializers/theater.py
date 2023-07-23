from cinemaccs_project.serializers import (
    TheaterSerializerBase,
    RoomSerializerBase,
    DescriptionElementSerializer,
    BrandSerializer
)


class TheaterSerializerGet(TheaterSerializerBase):
    brand = BrandSerializer(read_only=True)
    description_elements = DescriptionElementSerializer(
        read_only=True, many=True
    )
    rooms = RoomSerializerBase(many=True, read_only=True)
