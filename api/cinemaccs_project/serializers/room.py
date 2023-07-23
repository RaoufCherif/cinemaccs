from cinemaccs_project.serializers import (
    RoomSerializerBase,
    TheaterSerializerBase,
    DescriptionElementSerializer
)


class RoomSerializerGet(RoomSerializerBase):
    theater = TheaterSerializerBase(read_only=True)
    description_elements = DescriptionElementSerializer(
        read_only=True, many=True
    )
