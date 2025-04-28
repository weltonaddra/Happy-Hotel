from flask import Flask, render_template, jsonify
from services.test_service import TestService

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Initialize TestService
test_service = TestService()
test_service.create_fake_guests(20)
test_service.create_fake_rooms(10)
test_service.create_fake_reservations(20)

# Home page (Reservations)
@app.route('/')
def home():
    reservations = test_service.get_all_reservations()
    return render_template('layout.html', reservations=reservations, active_page='reservations')

# Guests page
@app.route('/guests')
def guests():
    guests = test_service.guests
    return render_template('guests.html', guests=guests, active_page='guests')

# Rooms page
@app.route('/rooms')
def rooms():
    rooms = test_service.rooms
    return render_template('rooms.html', rooms=rooms, active_page='rooms')

# API for reservations
@app.route('/api/reservations')
def get_reservations():
    return jsonify(test_service.get_all_reservations())

# API for guests
@app.route('/api/guests')
def get_guests():
    return jsonify([guest.__dict__ for guest in test_service.guests])

# API for rooms
@app.route('/api/rooms')
def get_rooms():
    return jsonify([room.__dict__ for room in test_service.rooms])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#flask run to run the app
#flask --app app.py --debug run
