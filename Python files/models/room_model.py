from typing import Literal

class Room:
    def __init__(self, room_number: int, room_type: Literal["Single", "Double", "Suite"], is_occupied: bool = False):
        self.room_number = room_number
        self.room_type = room_type
        self.is_occupied = is_occupied

    def to_dict(self):
        return self.__dict__