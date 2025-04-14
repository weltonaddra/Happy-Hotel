from models.guest import Guest

class GuestService:
    _guests = []

    @classmethod
    def add_guest(cls, guest_data):
        guest = Guest(**guest_data)
        cls._guests.append(guest)
        return guest

    @classmethod
    def get_all_guests(cls):
        return cls._guests

    @classmethod
    def find_guest_by_email(cls, email: str):
        for g in cls._guests:
            if g.email == email:
                return g
        return None
