from models.reservation import Reservation

class ReservationService:
    _reservations = []

    @classmethod
    def create_reservation(cls, reservation_data):
        reservation = Reservation(**reservation_data)
        cls._reservations.append(reservation)
        return reservation

    @classmethod
    def get_all_reservations(cls):
        return cls._reservations

    @classmethod
    def find_by_guest(cls, guest_id: int):
        results = []
        for r in cls._reservations:
            if r.guest_id == guest_id:
                results.append(r)
        return results

    @classmethod
    def cancel_reservation(cls, reservation_id: int):
        cls._reservations = [r for r in cls._reservations if r.id != reservation_id]
