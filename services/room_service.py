from models.room import Room

class RoomService:
    _rooms = []

    @classmethod
    def add_room(cls, room_data):
        room = Room(**room_data)
        cls._rooms.append(room)
        return room

    @classmethod
    def get_all_rooms(cls):
        return cls._rooms

    @classmethod
    def find_available_room(cls, room_type = None):
        for room in cls._rooms:
            if not room.is_occupied and (room_type is None or room.room_type == room_type):
                return room
        return None

    @classmethod
    def mark_as_occupied(cls, room_id: int):
        for room in cls._rooms:
            if room.id == room_id:
                room.is_occupied = True
                break

    @classmethod
    def mark_as_available(cls, room_id: int):
        for room in cls._rooms:
            if room.id == room_id:
                room.is_occupied = False
                break
