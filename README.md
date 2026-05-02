# 🌆 Smart City Dashboard (Cloud-Based)

## 📌 Overview

This project is a **cloud-based smart city monitoring system** that simulates and analyzes urban data such as **traffic, pollution, energy consumption, and waste management**.

The system uses cloud computing to store, process, and visualize data, providing insights like **alerts, trends, and predictions**.

---

## 🎯 Objective

* Centralize city data using cloud
* Perform real-time-like analysis
* Generate alerts for abnormal conditions
* Build a scalable smart city solution

---

## ⚙️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Cloud:** Google Cloud Platform (Firebase Firestore)
* **Data:** Kaggle datasets (simulated streaming)

---

## ☁️ Cloud Usage

This project uses **Firebase Firestore** as a cloud database to:

* Store simulated real-time data
* Enable centralized data access
* Support scalable architecture

---

## 🔄 Project Workflow

```text
Dataset → Simulator → Firestore (Cloud) → Backend APIs → Frontend Dashboard
```

---

## 🧩 Modules

### 1. 📊 Data Simulation

* Reads dataset
* Generates dynamic values
* Sends data to cloud every few seconds

### 2. ☁️ Cloud Database (Firestore)

* Stores:

  * traffic
  * pollution
  * energy
  * waste
* Acts as central data hub

### 3. ⚙️ Backend (Flask)

Provides APIs:

* `/latest` → latest values
* `/average` → average analysis
* `/alerts` → threshold alerts
* `/trend` → increasing/decreasing trends
* `/predict` → simple prediction

### 4. 📈 Frontend Dashboard

* Displays live data
* Shows alerts and trends
* Visualizes system output

---

## 📊 Features

* Real-time data simulation
* Cloud-based storage
* Alert system 🚨
* Trend analysis 📈
* Prediction (basic) 📉
* Modular architecture

---

## 🧪 How to Run

### 1. Install dependencies

```bash
pip install flask firebase-admin
```

### 2. Add Firebase Key

* Place `serviceAccountKey.json` in root folder
* (Not included in repo for security)

### 3. Run Simulator

```bash
cd simulator
python simulate.py
```

### 4. Run Backend

```bash
cd backend
python app.py
```

### 5. Open Frontend

Open `index.html` in browser

---

## 📊 Results

* Data successfully streamed to cloud
* Backend performs real-time analysis
* Alerts generated for high values
* Dashboard displays insights

---

## 🚀 Future Enhancements

* Cloud Functions for automation
* Firebase Hosting for deployment
* AI/ML prediction models
* BigQuery for advanced analytics
* Real IoT sensor integration

---

## 🔐 Security Note

Sensitive files like Firebase service keys are excluded using `.gitignore`.

---

## 🧠 Key Learning

* Cloud-based architecture design
* Real-time data simulation
* Backend API development
* Cloud database integration

---

## 📌 Conclusion

This project demonstrates how cloud computing can be used to build a **scalable, real-time smart city monitoring system**, integrating data collection, processing, and visualization.

---
