from faker import Faker
import random
from models.reservation_model import Reservation
from models.guest_model import Guest
from models.room_model import Room
from services.reservation_service import ReservationService

class TestService:
    def __init__(self):
        self.fake = Faker()
        self.reservation_service = ReservationService()
        self.guests = []
        self.rooms = []

    def create_fake_guests(self, count=10):
        for i in range(1, count + 1):
            guest = Guest(
                id=i,
                name=self.fake.name(),
                email=self.fake.email(),
                phone=self.fake.phone_number()
            )
            self.guests.append(guest)

    def create_fake_rooms(self, count=10):
        for i in range(1, count + 1):
            room = Room(
                room_number=random.randint(1, count),
                room_type=random.choice(["Single", "Double", "Suite"]),
                price_per_night=round(random.uniform(50.0, 500.0), 2),
                is_occupied=random.choice([True, False])
            )
            self.rooms.append(room)

    def create_fake_reservations(self, count=10):
        for i in range(1, count + 1):
            guest = random.choice(self.guests)
            room = random.choice(self.rooms)
            reservation = Reservation(
                res_id=i,
                guest_name=guest.name,
                room_number=room.room_number,
                check_in_date=self.fake.date_this_year(before_today=True, after_today=False),
                check_out_date=self.fake.date_this_year(before_today=False, after_today=True),
                total_price=round(random.uniform(100.0, 1000.0), 2)
            )
            self.reservation_service.add_reservation(reservation)

    def get_all_reservations(self):
        """Retrieve all reservations."""
        return self.reservation_service.get_all_reservations()

# Example usage
if __name__ == "__main__":
    test_service = TestService()
    test_service.create_fake_guests(10)
    test_service.create_fake_rooms(10)
    test_service.create_fake_reservations(10)

    print("Guests:")
    for guest in test_service.guests:
        print(guest)

    print("\nRooms:")
    for room in test_service.rooms:
        print(room)

    print("\nReservations:")
    reservations = test_service.get_all_reservations()
    for res in reservations:
        print(res)