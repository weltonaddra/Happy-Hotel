class Reservation:
    def __init__(self, res_id: int, guest_name: str, room_number: int, check_in_date: str, check_out_date: str , total_price: float = 0.0):
        self.res_id = res_id
        self.guest_name = guest_name
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = total_price


    def to_dict(self):
        return self.__dict__
