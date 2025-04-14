from typing import Literal

class Room:
    def __init__(self, id: int, room_number: str, room_type: Literal["Single", "Double", "Suite"], is_occupied: bool = False):
        self.id: int = id
        self.room_number: str = room_number
        self.room_type: str = room_type
        self.is_occupied: bool = is_occupied
