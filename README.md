# 🛡️ VayuNetra (वायुNetra)
### Tactical AI Drone Detection, Sensor Fusion & Airspace Defence C2 System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blue?style=flat)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey)](#)

**VayuNetra (वायुNetra)** is a military-grade Command & Control (C2) situational awareness and counter-unmanned aerial system (C-UAS) platform. It provides automated real-time drone detection, multi-sensor kinematic fusion, 3D trajectory forecasting, automated threat evaluation, and pan-tilt tracking gimbal control.

---

## 📌 Key Architectural Pillars

```
                     +---------------------------------------+
                     |           Sensor Ingestion            |
                     |  (USB / FLIR Video + FMCW Radar Data) |
                     +-------------------+-------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |      AI Vision & Detection Engine     |
                     |      (YOLOv8 + ByteTrack Tracker)     |
                     +-------------------+-------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |    Kinematic Fusion & Threat Matrix   |
                     |  (EKF State Estimation + CV Predictor)|
                     +-------------------+-------------------+
                                         |
                   +---------------------+---------------------+
                   |                                           |
                   v                                           v
     +---------------------------+               +---------------------------+
     |   Real-Time C2 Frontend   |               | Hardware Gimbal / Pan-Tilt|
     | (WebSocket Telemetry HUD) |               |  (ESP32 Serial PID Servos)|
     +---------------------------+               +---------------------------+
```

---

## 🚀 Features

### 1. 👁️ AI Computer Vision & Neural Target Acquisition
- **Real-Time Drone Detection**: Optimized YOLOv8 models for micro, nano, fixed-wing, and rotary-wing UAS classification.
- **Multi-Object Tracking**: ByteTrack / SORT tracking maintaining persistent Target IDs across occlusion and rapid maneuvers.
- **Multi-Modal Vision Modes**: Live AI Stream, Simulated Thermal FLIR (White-Hot), Night Vision (NVG Green), and Day Optical.
- **Recorded Video Ingestion**: Built-in drag-and-drop / file upload engine for post-mission video analysis and field drone footage verification.

### 2. 📡 Tactical Radar Scope & Sensor Fusion
- **200m Tactical Airspace Big Board**: 360° PPI (Plan Position Indicator) radar sweep with distance rings and range markers.
- **Kinematic Sensor Fusion**: Extended Kalman Filter (EKF) combining optical bearing/elevation with FMCW radar Doppler velocities.
- **Defensive Engagement Zones**: Configurable engagement perimeters with visual breach alerts (Warning Zone @ 120m, Critical Zone @ 50m).

### 3. 📈 3D Isometric Trajectory Forecasting
- **Future Path Prediction**: Constant-Velocity (CV) EKF predicting +3.0s future spatial waypoint coordinates.
- **Multi-View Projections**: Seamless switching between **3D Isometric**, **Lateral (X-Z)**, and **Vertical (Y-Z)** flight profiles.
- **Covariance Envelope**: Visualizes target position uncertainty and trajectory intercept cones.

### 4. ⚡ TEWA Threat Evaluation & Priority Matrix
- **Automated Threat Scoring**: Dynamic algorithm weighing target proximity, closure velocity, heading vector, and AI classification confidence.
- **Target Categorization**: Real-time classification into **NOMINAL**, **ELEVATED**, and **CRITICAL** danger tiers with Time-to-Impact (TTI) metrics.
- **Master Air Picture Table**: Live sortable target matrix with one-click CSV mission data export.

### 5. 🎯 Hardware Pan-Tilt Gimbal & Microcontroller Interface
- **ESP32 Firmware**: Dual-axis microsecond-precision servo control over UART/USB serial bridge.
- **Closed-Loop PID Tracking**: Automated optical boresight lock centering camera optics onto high-priority airborne targets.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **AI / Machine Learning** | YOLOv8 (Ultralytics), PyTorch, ByteTrack, OpenCV, FilterPy (EKF) |
| **Backend & APIs** | Python 3.11+, FastAPI, Uvicorn, WebSockets, AsyncIO, PySerial |
| **Frontend & UI/UX** | HTML5 Canvas, Vanilla JS, CSS3 Design Tokens (Charcoal Command Console theme) |
| **Typography** | Barlow Condensed (Headings), IBM Plex Mono (Telemetry & Values), Inter (Body) |
| **Firmware & Hardware** | ESP32, C++ / Arduino IDE, Micro-Servos, FMCW Radar / Simulator |
| **Database** | SQLite, PostgreSQL (asyncpg schema ready) |

---

## 📁 Repository Structure

```
VayuNetra/
├── backend/
│   ├── cyber_defense/         # RF signal monitoring & jamming simulation
│   ├── fusion/                # Extended Kalman Filter, Threat Matrix & Trajectory
│   ├── gimbal/                # Servo PID controller & tracking calculations
│   ├── hardware/              # ESP32 serial bridge & FMCW radar interface
│   ├── vision/                # YOLOv8 detector, tracker & velocity estimator
│   ├── config.py              # Central system configuration & thresholds
│   ├── main.py                # FastAPI app, MJPEG stream & WebSocket broadcaster
│   ├── requirements.txt       # Python dependencies
│   └── simulator.py           # Synthetic multi-target tactical radar simulator
├── database/
│   ├── db_manager.py          # SQLite / async database persistence manager
│   └── schema.sql             # Relational schema for mission event logs
├── firmware/
│   ├── esp32_servo_tracker/   # Dual-axis servo tracker Arduino source
│   └── esp32_smart_shield/    # Primary hardware interface firmware
├── frontend/
│   ├── js/
│   │   ├── gimbal_controls.js # Hardware gimbal manual & auto controls
│   │   ├── optical_hud.js     # Canvas FLIR/NVG optical HUD renderer
│   │   ├── radar_scope.js     # 200m tactical radar Canvas engine
│   │   ├── rf_spectrum.js     # RF spectrum waterfall & countermeasure monitor
│   │   └── trajectory_viz.js  # 3D isometric & 2D trajectory prediction engine
│   ├── app.js                 # WebSocket client, C2 state coordinator & UI dispatcher
│   ├── index.html             # C2 Command Warroom dashboard layout
│   ├── styles.css             # Charcoal command console design tokens & styles
│   └── vayu_netra_logo.jpg    # Emblem & branding asset
├── smart_shield_ai/           # Pre-trained models, risk engines & event logging
├── tests/                     # Automated unit and integration test suite
├── yolov8n.pt                 # Core lightweight detection neural network
├── vercel.json                # Cloud deployment configuration
└── .gitignore                 # Standard Python/IDE ignore rules
```

---

## ⚙️ Quickstart & Local Setup

### 1. Prerequisites
- Python 3.10+ installed
- Git
- Web camera or USB video capture device (optional; simulator fallback included)

### 2. Clone Repository
```bash
git clone https://github.com/Ayushanibarik/VayuNetra.git
cd VayuNetra
```

### 3. Create Virtual Environment & Install Dependencies
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Linux/macOS:
source .venv/bin/activate

pip install -r backend/requirements.txt
```

### 4. Launch VayuNetra C2 Server
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### 5. Access the C2 Console
Open your browser and navigate to:
```
http://localhost:8000/
```

---

## 🎮 Operational Workflow

1. **System Startup**: Upon loading, the backend establishes real-time WebSocket telemetry (`/ws/telemetry`) and launches the live AI inference worker thread.
2. **Video Ingestion**: Click `📁 UPLOAD VIDEO` to ingest recorded drone test flights, or connect a live USB webcam for real-time field surveillance.
3. **Radar & Fusion**: Observe targets tracked simultaneously on the **Tactical Airspace Radar Scope** (left) and the **3D Trajectory Forecaster** (right).
4. **Threat Assessment**: High-risk targets entering defensive perimeters automatically trigger elevated threat levels in the **Threat Matrix** and **TEWA Air Picture Table**.
5. **Mission Export**: Click `📊 EXPORT CSV` to save tactical telemetry, timestamps, and threat scores for post-mission debriefing.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
