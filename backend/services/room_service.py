from models.room_model import Room

class RoomService:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room: Room):
        self.rooms[room.room_number] = room

    def get_room_by_number(self, room_number: int) -> Room:
        return self.rooms.get(room_number)

    def get_all_rooms(self) -> list:
        return [room.to_dict() for room in self.rooms.values()]

    def get_all_rooms(self) -> list[dict]:
        return [room.to_dict() for room in self._rooms]
    

    def find_available_room(self, room_type: str = None) -> Room | None: #Returns a room object or None
        for room in self._rooms:
            if not room.is_occupied and (room_type is None or room.room_type == room_type):
                return room
        return None

    def mark_as_occupied(self, room_number: int):
        room = self.get_room_by_number(room_number)
        if room:
            room.is_occupied = True

    def mark_as_available(self, room_number: int):
        room = self.get_room_by_number(room_number)
        if room:
            room.is_occupied = False