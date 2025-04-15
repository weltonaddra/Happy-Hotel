from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask in Codespaces!"

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    # Replace with actual database query
    rooms = [
        {"id": 1, "name": "Room A"},
        {"id": 2, "name": "Room B"},
        {"id": 3, "name": "Room C"}
    ] 
    return {"rooms": rooms}

def about():    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#look for github actions and dependabot to check packages
#Package control