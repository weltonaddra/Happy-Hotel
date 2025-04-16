from models.guest_model import Guest

class GuestService:
    def __init__(self):
        self._guests: dict[int, Guest] = {}

    def add_guest(self, guest: Guest):
        self._guests[guest.id] = guest

    def get_guest_by_id(self, guest_id: int) -> Guest | None:
        return self._guests.get(guest_id)

    def get_all_guests(self):
        return [guest.to_dict() for guest in self._guests.values()]
