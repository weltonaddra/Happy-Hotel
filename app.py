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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#flask run to run the app
#flask --app app.py --debug run
