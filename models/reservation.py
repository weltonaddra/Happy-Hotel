class Reservation:
    def __init__(self, id: int, guest_id: int, room_id: int, check_in_date: str, check_out_date: str):
        self.id: int = id
        self.guest_id: int = guest_id
        self.room_id: int = room_id
        self.check_in_date: str = check_in_date
        self.check_out_date: str = check_out_date
