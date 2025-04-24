from flask import Blueprint, jsonify
from services.room_service import RoomService
from models.room_model import Room

room_routes = Blueprint('room_routes', __name__)
room_service = RoomService()

# Example data to start with
room_service.add_room(Room(101, "Single"))
room_service.add_room(Room(102, "Double"))
room_service.add_room(Room(103, "Suite", True))

@room_routes.route('/api/rooms/<int:room_number>', methods=['GET'])
def get_room(room_number):
    room = room_service.get_room_by_number(room_number)
    if room:
        return jsonify(room.to_dict())
    return jsonify({"error": "Room not found"}), 404

@room_routes.route('/api/rooms', methods=['GET'])
def get_all_rooms():
    return jsonify(room_service.get_all_rooms())
