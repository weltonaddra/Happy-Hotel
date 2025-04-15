class Reservation:
    def __init__(self, id: int, guest_id: int, room_id: int, check_in_date: str, check_out_date: str):
        self.id = id
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def to_dict(self):
        return self.__dict__
