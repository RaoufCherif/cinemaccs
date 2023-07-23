from cinemaccs_project.serializers import (
    TheaterSerializerNoRooms,
    RoomSerializerNoTheater,
)


class TheaterSerializer(TheaterSerializerNoRooms):
    rooms = RoomSerializerNoTheater(many=True, read_only=True)
