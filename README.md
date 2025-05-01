# 🏨 Happy-Hotel

Happy-Hotel is a hotel management system designed to manage reservations, guests, and rooms efficiently. It includes a backend API, a frontend user interface, and supporting services.

---

## 📑 Table of Contents

1. [📂 Project Structure](#-project-structure)
2. [⚙️ Setup Instructions](#️-setup-instructions)
3. [🚀 Usage](#-usage)
4. [📜 File Descriptions](#-file-descriptions)

---

## 📂 Project Structure

Happy-Hotel/ ├── backend/ # 🛠️ Backend API and services │ ├── app.py # 🚪 Main backend application │ ├── models/ # 🗄️ Database models │ ├── routes/ # 🌐 API routes │ ├── services/ # 🧠 Business logic services ├── frontend/ # 🎨 Frontend user interface │ ├── static/ # 📁 Static assets (CSS, JS, images) │ ├── templates/ # 🖼️ HTML templates ├── venv/ # 🐍 Python virtual environment ├── package.json # 📦 Frontend dependencies ├── requirements.txt # 📋 Backend dependencies ├── README.md # 📖 Project documentation


---

## ⚙️ Setup Instructions

### 🛠️ Backend Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
Run the backend server:
python backend/app.py
🎨 Frontend Setup
Install Node.js dependencies:

npm install
Run the frontend server:

npm start
🚀 Usage
Start the backend server.
Start the frontend server.
Access the application in your browser at http://localhost:3000.
📜 File Descriptions
🛠️ Backend
backend/app.py: 🚪 Entry point for the backend application.
backend/models/: 🗄️ Contains database models:
guest_model.py: Guest-related data structure.
reservation_model.py: Reservation-related data structure.
room_model.py: Room-related data structure.
backend/routes/: 🌐 API endpoints:
guest_routes.py: Guest-related API routes.
reservations_routes.py: Reservation-related API routes.
room_routes.py: Room-related API routes.
backend/services/: 🧠 Business logic:
guest_service.py: Guest-related logic.
reservation_service.py: Reservation-related logic.
🎨 Frontend
frontend/static/: 📁 Contains static assets:
css/: 🎨 Stylesheets (e.g., style.css, oldStyle.css).
js/: ⚙️ JavaScript files (e.g., mainJS.js, widgets.js).
frontend/templates/: 🖼️ HTML templates for rendering pages:
index.html: Main page template.
base.html: Base template for shared layout.
📋 Other Files
requirements.txt: 📋 Python dependencies for the backend.
package.json: 📦 Node.js dependencies for the frontend.
README.md: 📖 Project documentation.
Feel free to customize this documentation further based on your specific needs! 🎉 ```