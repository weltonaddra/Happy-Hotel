from models.reservation_model import Reservation

class ReservationService:
    def __init__(self):
        self._reservations: dict[int, Reservation] = {}

    def add_reservation(self, reservation: Reservation):
        self._reservations[reservation.id] = reservation

    def get_reservation_by_id(self, reservation_id: int) -> Reservation | None:
        return self._reservations.get(reservation_id)

    def get_all_reservations(self):
        return [res.to_dict() for res in self._reservations.values()]
