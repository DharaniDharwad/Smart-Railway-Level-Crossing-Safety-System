# Smart-Railway-Level-Crossing-Safety-System
Arduino-based smart railway level crossing safety system with two-stage train detection, automatic gate control, safety indicators, and a Python visual monitoring dashboard.

# 🚆 Smart Railway Level Crossing Safety System Using Arduino

A simulation-based **Smart Railway Level Crossing Safety System** designed to automate railway gate control using two-stage train detection. The system detects an approaching train, closes both crossing gates, keeps them closed while the train passes through the crossing, and reopens them only after the complete train has cleared the second detection zone.

The project is implemented using **Arduino Uno and Wokwi simulation**, with a **Python Tkinter visual dashboard** for real-time monitoring and visualization.

## 📌 Project Overview

Railway level crossings can be dangerous when road traffic enters the crossing while a train is approaching or passing through.

This project demonstrates an automated control system in which train movement is monitored using two detection points:

**Detection 1** is positioned before the railway crossing. When the front of the train reaches Detection 1, both gates close immediately.

The train then continues moving through the crossing while the gates remain closed.

**Detection 2** is positioned after the crossing. It confirms that the complete train has passed the crossing. Only after this detection do both gates open and the system return to the safe state.

> **Note:** This project is an educational prototype/simulation and is not intended for direct deployment in real railway infrastructure.

## 🎯 Objectives

* Automate railway crossing gate control.
* Detect an approaching train before it reaches the crossing.
* Close both gates immediately after the first detection.
* Keep the gates closed while the train passes through the crossing.
* Confirm complete train clearance using a second detection point.
* Automatically reopen both gates after the train has completely passed.
* Provide visual safety indications using red and green LEDs.
* Display system status using a 16×2 I2C LCD.
* Provide a Python-based visual monitoring dashboard.

## ⚙️ System Working

The system follows a two-stage detection mechanism.

### 1. Normal Condition

When no train is detected:

* Both gates remain open.
* Green safety indication is ON.
* Red warning indication is OFF.
* The system displays a safe/clear status.

### 2. Detection 1 – Train Approaching

When the front of the train reaches the first detection zone:

* The train is detected.
* Both gates close immediately.
* Red warning indication is activated.
* Green safety indication is turned OFF.
* The train continues moving toward and through the crossing.

### 3. Train Passing Through Crossing

While the train is moving through the crossing:

* Both gates remain closed.
* The system remains in the warning/occupied state.
* The train continues moving toward the second detection zone.

### 4. Detection 2 – Train Completely Cleared

When the rear of the train passes the second detection zone:

* The system confirms that the train has completely cleared the crossing.
* Both gates open automatically.
* Red warning indication is turned OFF.
* Green safety indication is activated.
* The system returns to the safe state.

## 🔄 System Flow
             START
               │
               ▼
       Initialize System
               │
               ▼
       Gates Open / SAFE
               │
               ▼
      Train Approaches
               │
               ▼
        ┌─────────────┐
        │ Detection 1 │
        └─────────────┘
               │
               ▼
       Both Gates CLOSE
               │
               ▼
       Red Signal ON
       Green Signal OFF
               │
               ▼
        Train Crosses
       Railway Crossing
               │
               ▼
        ┌─────────────┐
        │ Detection 2 │
        └─────────────┘
               │
               ▼
    Train Completely Cleared
               │
               ▼
       Both Gates OPEN
               │
               ▼
       Green Signal ON
               │
               ▼
          SAFE STATE

## 🧩 System Architecture

                 ┌─────────────────────┐
                 │      Train          │
                 │      Movement       │
                 └──────────┬──────────┘
                            │
                            ▼
                   ┌────────────────┐
                   │  Detection 1   │
                   └───────┬────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   Arduino Uno    │
                  │  Control Logic   │
                  └───────┬──────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
    ┌──────────┐    ┌───────────┐    ┌──────────┐
    │  Gates   │    │   LEDs    │    │  Buzzer  │
    │  Control │    │ Red/Green │    │ Warning  │
    └──────────┘    └───────────┘    └──────────┘
          │
          ▼
    ┌──────────────┐
    │  LCD Display │
    └──────────────┘

                   Train continues
                         │
                         ▼
                ┌────────────────┐
                │  Detection 2   │
                └───────┬────────┘
                        │
                        ▼
                  Train Cleared
                        │
                        ▼
                   Gates OPEN


## 🛠️ Hardware Components
| Component    | Quantity | Purpose                   |
| ------------ | -------: | ------------------------- |
| Arduino Uno  |        1 | Main controller           |
| 16×2 I2C LCD |        1 | Displays system status    |
| Servo Motor  |        2 | Controls railway gates    |
| Push Button  |        2 | Simulates train detection |
| Red LED      |        1 | Warning/stop indication   |
| Green LED    |        1 | Safe indication           |
| Buzzer       |        1 | Audible warning           |
| Resistors    |        2 | LED current limiting      |
| Wokwi        |        — | Circuit simulation        |

## 🔌 Pin Configuration
| Component                  | Arduino Pin | Function                  |
| -------------------------- | ----------- | ------------------------- |
| Detection 1 / Entry Sensor | D2          | Detects approaching train |
| Detection 2 / Exit Sensor  | D3          | Confirms train clearance  |
| Red LED                    | D5          | Warning indication        |
| Green LED                  | D6          | Safe indication           |
| Buzzer                     | D7          | Warning sound             |
| Servo Gate                 | D9          | Gate control              |
| LCD SDA                    | A4          | I2C data                  |
| LCD SCL                    | A5          | I2C clock                 |
| LCD VCC                    | 5V          | Power                     |
| LCD GND                    | GND         | Ground                    |

> The push buttons are used as simulated train detection sensors in the prototype.

## 💻 Software & Technologies

* **Arduino**
* **Embedded C / Arduino C++**
* **Wokwi**
* **Python**
* **Tkinter**
* **I2C communication**
* **Servo motor control**
* **Serial monitoring**

## 🖥️ Python Visual Dashboard

A Python-based **Tkinter dashboard** was developed to provide a visual representation of the railway crossing system.

The dashboard includes:

* 🚆 Train movement simulation
* 🚦 Red and green safety signals
* 🚧 Two railway gates
* 📍 Detection 1 and Detection 2
* 📊 System status monitoring
* 🔊 Buzzer status
* 🔄 Reset functionality
* ▶ Train start control
* Visual representation of the complete crossing sequence

### Dashboard Sequence
Train starts far from crossing
             ↓
       Detection 1
             ↓
       Gates CLOSE
             ↓
    Train keeps moving
             ↓
      Gate 1 crossed
             ↓
      Gate 2 crossed
             ↓
       Detection 2
             ↓
       Gates OPEN
             ↓
        System SAFE


## ▶️ How to Run the Arduino Simulation
### Step 1 — Open Wokwi
Create/open the Arduino Uno simulation in Wokwi.

### Step 2 — Add the Components
Add:
* Arduino Uno
* I2C LCD
* Servo motors
* LEDs
* Buzzer
* Push buttons

### Step 3 — Upload the Arduino Code
Open:
Arduino/railway_crossing.ino
Copy the code into the Wokwi Arduino project.

### Step 4 — Start Simulation
Run the Wokwi simulation and use the detection buttons to simulate train movement.

### Dashboard Controls
| Button               | Function                  |
| -------------------- | ------------------------- |
| ▶ START TRAIN        | Starts train movement     |
| ● SIMULATE DETECTION | Simulates train detection |
| ↻ RESET SYSTEM       | Resets the system         |

## 📊 Expected Output
### 🟢 Safe State
TRAIN: NO
GATE: OPEN
RED: OFF
GREEN: ON
BUZZER: OFF
STATUS: SAFE

### 🔴 Train Detected
TRAIN: DETECTED
GATE: CLOSED
RED: ON
GREEN: OFF
BUZZER: ON
STATUS: CROSSING OCCUPIED

### 🟢 Train Completely Passed
TRAIN: PASSED
GATE: OPEN
RED: OFF
GREEN: ON
BUZZER: OFF
STATUS: SAFE

## 🎥 Demonstration
A demonstration video can show the complete sequence:

Train starts
     ↓
Detection 1
     ↓
Both gates close
     ↓
Train crosses the crossing
     ↓
Detection 2
     ↓
Both gates open
     ↓
Safe status

## 💡 Key Learning Outcomes
Through this project, I gained practical experience in:
* Arduino programming
* Embedded C/C++ programming
* Digital input and output control
* I2C LCD interfacing
* Servo motor control
* Sensor-based automation
* State-based system logic
* Real-time system monitoring
* Wokwi simulation
* Python Tkinter GUI development
* Integrating embedded-system concepts with a visual monitoring interface

## 🚀 Future Enhancements
The current implementation is a simulation/prototype. Possible future improvements include:
* Replacing push buttons with real IR, ultrasonic, or other suitable train-detection sensors.
* Adding physical railway gate mechanisms.
* Adding obstacle detection at the crossing.
* Adding train speed and distance monitoring.
* Adding emergency/manual override functionality.
* Adding IoT-based remote monitoring.
* Adding event logging and historical data.
* Implementing additional fault-detection mechanisms.

## ⚠️ Limitations
* The current project is implemented as a simulation/prototype.
* Push buttons are used to represent train detection sensors.
* The Python dashboard is a visual simulation.
* The system has not been tested in an actual railway environment.
* The prototype is not intended for railway-grade safety deployment.

## 📜 License
This project is intended for **educational and learning purposes**.

You are welcome to explore and modify the project for academic and educational use.
