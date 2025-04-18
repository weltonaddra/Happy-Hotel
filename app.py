from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')  # This looks for templates/index.html

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    # Example static room data; in reality you'd get this from a database or service
    rooms = [
        {"id": 1, "name": "Room A"},
        {"id": 2, "name": "Room B"},
        {"id": 3, "name": "Room C"}
    ]
    return jsonify({"rooms": rooms})

reservations = [
    {"guest_name": "John Doe", "room": 101, "checkin": "2025-04-15", "checkout": "2025-04-18"},
    {"guest_name": "Jane Smith", "room": 202, "checkin": "2025-04-16", "checkout": "2025-04-19"}
]

@app.route("/api/reservations")
def get_reservations():
    return jsonify(reservations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#flask run to run the app
#flask --app app.py --debug run
