from flask import Blueprint, jsonify, request
from services.guest_service import GuestService
from models.guest_model import Guest

guest_bp = Blueprint("guest", __name__)
guest_service = GuestService()

@guest_bp.route("/guests", methods=["GET"])
def get_all_guests():
    return jsonify(guest_service.get_all_guests())

@guest_bp.route("/guests/<int:guest_id>", methods=["GET"])
def get_guest(guest_id):
    guest = guest_service.get_guest_by_id(guest_id)
    if guest:
        return jsonify(guest.to_dict())
    return jsonify({"error": "Guest not found"}), 404

@guest_bp.route("/guests", methods=["POST"])
def add_guest():
    data = request.json
    try:
        guest = Guest(**data)
        guest_service.add_guest(guest)
        return jsonify({"message": "Guest added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
