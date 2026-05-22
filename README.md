# 🎓 Smart Attendance System

> Automated attendance tracking powered by real-time facial recognition — built for classrooms and corporate environments.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

Smart Attendance is a desktop application that replaces manual roll-calls with a fully automated, face-recognition-based attendance pipeline. Using your webcam, it registers students/employees, trains a local face model, and marks attendance into CSV files — all through a clean Tkinter GUI.

---

## ✨ Features

- **Face Registration** — Capture 100 face samples per person via webcam
- **LBPH Face Training** — Trains a Local Binary Patterns Histogram model on registered faces
- **Real-Time Recognition** — Identifies faces live from the webcam feed
- **Automatic CSV Logging** — Saves daily attendance files with ID, name, date, and time
- **Password Protection** — Secure the training step with a password; supports password change
- **Live Clock** — Displays current time in the UI

---

## 🖼️ Screenshot

![Taking Attendance](Taking%20Attendance.png)

---

## 🗂️ Project Structure

Smart-Attendance/

├── main.py                              # Main application
 
├── haarcascade_frontalface_default.xml  # Haar Cascade for face detection (required)
 
├── install commands .txt                # Dependency list

├── TrainingImage/                       # Auto-created: captured face images

├── TrainingImageLabel/                  # Auto-created: trained model & password

│   ├── Trainner.yml

│   └── psd.txt

├── StudentDetails/                      # Auto-created: student/employee registry

│   └── StudentDetails.csv

└── Attendance/                          # Auto-created: daily attendance CSVs

└── Attendance_YYYY-MM-DD.csv

---

## ⚙️ Prerequisites

- Python 3.x
- A working webcam
- [`haarcascade_frontalface_default.xml`](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) — place it in the project root

---

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/Harshith0906/Smart-Attendance.git
cd Smart-Attendance
```

**2. Install dependencies**
```bash
pip install tk-tools opencv-contrib-python numpy pillow pandas times
```

**3. Download the Haar Cascade**

Download [`haarcascade_frontalface_default.xml`](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in the project root.

> `datetime`, `csv`, and `os` are part of the Python standard library — no separate install needed.

**4. Run the application**
```bash
python main.py
```

---

## 🧭 Usage

### Step 1 — Register a Person
1. Enter the person's **ID** and **Name** in the left panel.
2. Click **Take Images** — the webcam opens and captures 100 face samples automatically.
3. Press `q` to stop early if needed.

### Step 2 — Train the Model
1. Click **Save Profile**.
2. Enter the password when prompted (you'll be asked to set one on first use).
3. The LBPH model trains on all registered faces and saves to `TrainingImageLabel/Trainner.yml`.

### Step 3 — Take Attendance
1. Click **Take Attendance**.
2. The webcam opens and recognises faces in real time.
3. Press `q` to stop — attendance is saved to `Attendance/Attendance_<date>.csv`.

### Changing the Password
Use the **Change Password** option in the UI to update the training password at any time.

---

## 📄 Output Format

Each session creates or appends to a CSV named `Attendance_YYYY-MM-DD.csv`:

| ID  | Name  | Date       | Time     |
|-----|-------|------------|----------|
| 101 | Alice | 2024-09-01 | 09:05:32 |
| 102 | Bob   | 2024-09-01 | 09:06:11 |

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|------------------|-------------------------------------|
| Language         | Python 3                            |
| GUI              | Tkinter                             |
| Face Detection   | OpenCV Haar Cascades                |
| Face Recognition | OpenCV LBPH (`opencv-contrib-python`) |
| Image Processing | Pillow, NumPy                       |
| Data Handling    | Pandas, CSV                         |

---

## 🔮 Potential Improvements

- [ ] Add a database backend (SQLite / MySQL) instead of CSV files
- [ ] Export attendance reports as PDF or Excel
- [ ] Add anti-spoofing / liveness detection
- [ ] Web dashboard for attendance analytics
- [ ] Multi-camera support

---

## 📬 Contact

For questions or support — **harshith0929@gmail.com**
