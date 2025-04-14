class Guest:
    def __init__(self, id: int, name: str, email: str, room_id: int, check_in_date: str, check_out_date: str = ""):
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.room_id: int = room_id
        self.check_in_date: str = check_in_date
        self.check_out_date: str = check_out_date
