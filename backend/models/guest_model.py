class Guest:
    def __init__(self, id: int, name: str, email: str, room_id: int, check_in_date: str, check_out_date: str = ""):
        self.id = id
        self.name = name
        self.email = email


    def to_dict(self):
        return self.__dict__
