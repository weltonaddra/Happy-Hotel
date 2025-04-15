from flask import Blueprint, jsonify, request
from services.reservation_service import ReservationService
from models.reservation_model import Reservation

reservation_bp = Blueprint("reservation", __name__)
reservation_service = ReservationService()

@reservation_bp.route("/reservations", methods=["GET"])
def get_all_reservations():
    return jsonify(reservation_service.get_all_reservations())

@reservation_bp.route("/reservations/<int:reservation_id>", methods=["GET"])
def get_reservation(reservation_id):
    res = reservation_service.get_reservation_by_id(reservation_id)
    if res:
        return jsonify(res.to_dict())
    return jsonify({"error": "Reservation not found"}), 404

@reservation_bp.route("/reservations", methods=["POST"])
def add_reservation():
    data = request.json #This takes a JSON body from an api post request
    try:
        reservation = Reservation(**data) #Creates new reservation object and passes each key in the JSON body as a parameter
        reservation_service.add_reservation(reservation)
        return jsonify({"message": "Reservation added successfully"}), 201
    except Exception as e:
        return jsonify({"error in reservations_routes add_reservation": str(e)}), 400
