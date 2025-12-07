# Happy-Hotel

A comprehensive hotel management system designed to streamline reservations, guest management, and room operations with an efficient backend API and intuitive frontend interface.

---

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [File Descriptions](#file-descriptions)
6. [Technologies Used](#technologies-used)

---

## Features

- **Reservation Management**: Create, view, and manage guest reservations
- **Guest Services**: Comprehensive guest information and service tracking
- **Room Management**: Real-time room status and availability tracking
- **User-Friendly Interface**: Intuitive frontend for seamless operations
- **RESTful API**: Robust backend with well-documented endpoints

---

## Project Structure

```
Happy-Hotel/
├── backend/
│   ├── app.py                 # Backend entry point
│   ├── models/                # Database models
│   │   ├── guest_model.py
│   │   ├── reservation_model.py
│   │   └── room_model.py
│   ├── routes/                # API endpoints
│   │   ├── guest_routes.py
│   │   ├── reservations_routes.py
│   │   └── room_routes.py
│   └── services/              # Business logic
│       ├── guest_service.py
│       └── reservation_service.py
├── frontend/
│   ├── static/                # Static assets
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── oldStyle.css
│   │   └── js/
│   │       ├── mainJS.js
│   │       └── widgets.js
│   └── templates/             # HTML templates
│       ├── base.html
│       └── index.html
├── requirements.txt           # Python dependencies
├── package.json              # Node.js dependencies
└── README.md                 # This file
```

---

## Setup Instructions

### Backend Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the backend server**:
   ```bash
   python backend/app.py
   ```

### Frontend Setup

1. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

2. **Run the frontend server**:
   ```bash
   npm start
   ```

---

## Usage

1. **Start the backend server** (default port: 5000)
2. **Start the frontend server** (default port: 3000)
3. **Access the application** in your browser at `http://localhost:3000`
4. **Begin managing** your hotel operations efficiently!

---

## File Descriptions

### Backend Components

| File/Folder | Description |
|------------|-------------|
| `backend/app.py` | Main application entry point and server configuration |
| `backend/models/` | Database models defining data structures |
| `backend/models/guest_model.py` | Guest-related data structure and validation |
| `backend/models/reservation_model.py` | Reservation-related data structure and logic |
| `backend/models/room_model.py` | Room-related data structure and status management |
| `backend/routes/` | RESTful API endpoints for frontend communication |
| `backend/routes/guest_routes.py` | Guest management API routes |
| `backend/routes/reservations_routes.py` | Reservation management API routes |
| `backend/routes/room_routes.py` | Room management API routes |
| `backend/services/` | Business logic and data processing |
| `backend/services/guest_service.py` | Guest-related business logic and operations |
| `backend/services/reservation_service.py` | Reservation-related business logic and workflows |

### Frontend Components

| File/Folder | Description |
|------------|-------------|
| `frontend/static/` | Static assets (CSS, JavaScript, images) |
| `frontend/static/css/` | Stylesheets for UI styling and responsiveness |
| `frontend/static/css/style.css` | Main stylesheet with modern design |
| `frontend/static/css/oldStyle.css` | Legacy stylesheet (for reference) |
| `frontend/static/js/` | JavaScript files for interactivity |
| `frontend/static/js/mainJS.js` | Main JavaScript application logic |
| `frontend/static/js/widgets.js` | UI widgets and component scripts |
| `frontend/templates/` | HTML templates for page rendering |
| `frontend/templates/base.html` | Base template with shared layout elements |
| `frontend/templates/index.html` | Main application page template |

### Configuration Files

| File | Description |
|------|-------------|
| `requirements.txt` | Python package dependencies for backend |
| `package.json` | Node.js dependencies and scripts for frontend |
| `README.md` | Comprehensive project documentation |

---

## Technologies Used

### Backend
- **Python**: Core backend programming language
- **Flask**: Web framework for API development
- **SQLAlchemy**: Database ORM (if applicable)

### Frontend
- **Node.js**: JavaScript runtime environment
- **HTML5**: Markup language for structure
- **CSS3**: Styling and responsive design
- **JavaScript**: Interactive functionality

---

## Getting Started

Ready to streamline your hotel operations? Follow the setup instructions above and you'll be up and running in minutes! For questions or support, please refer to the project documentation or contact the development team.

---

*Happy-Hotel - Making hotel management simple and efficient*
