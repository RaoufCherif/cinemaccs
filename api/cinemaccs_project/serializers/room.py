from cinemaccs_project.serializers import (
    RoomSerializerNoTheater,
    TheaterSerializerNoRooms
)


class RoomSerializer(RoomSerializerNoTheater):
    theater = TheaterSerializerNoRooms(read_only=True)
