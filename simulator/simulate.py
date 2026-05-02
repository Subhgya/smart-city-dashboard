import pandas as pd
import time
import random
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore

# ================= FIREBASE SETUP =================
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Firebase connected ✅")

# ================= LOAD DATASETS =================
pollution_df = pd.read_csv("pollution.csv")
traffic_df = pd.read_csv("traffic.csv")
energy_df = pd.read_csv("energy.csv")
waste_df = pd.read_csv("waste.csv")

# ================= CLEAN DATA =================

# Pollution
pollution_df = pollution_df.rename(columns={"City": "area", "AQI": "value"})
pollution_df = pollution_df[["area", "value"]].dropna()

# Traffic
traffic_df = traffic_df.rename(columns={"traffic_volume": "value"})
traffic_df["area"] = "City Center"
traffic_df = traffic_df[["area", "value"]]

# Energy
energy_df = energy_df.rename(columns={"Global_active_power": "value"})
energy_df["area"] = "Grid"
energy_df = energy_df[["area", "value"]].dropna()

# Waste
waste_df = waste_df.rename(columns={"country": "zone", "waste_generation": "fill"})
waste_df["type"] = "General"
waste_df = waste_df[["zone", "fill", "type"]].dropna()

print("Datasets loaded & cleaned ✅")

# ================= SIMULATION LOOP =================
while True:
    timestamp = datetime.now()

    p = pollution_df.sample(1).iloc[0]
    t = traffic_df.sample(1).iloc[0]
    e = energy_df.sample(1).iloc[0]
    w = waste_df.sample(1).iloc[0]

    db.collection("pollution").add({
        "area": p["area"],
        "value": int(p["value"] + random.randint(-10, 10)),
        "timestamp": timestamp
    })

    db.collection("traffic").add({
        "area": t["area"],
        "value": int(t["value"] + random.randint(-50, 50)),
        "timestamp": timestamp
    })

    db.collection("energy").add({
        "area": e["area"],
        "value": float(e["value"]),
        "timestamp": timestamp
    })

    db.collection("waste").add({
        "zone": w["zone"],
        "fill": int(w["fill"] + random.randint(-5, 5)),
        "type": w["type"],
        "timestamp": timestamp
    })

    print("Streaming data to cloud 🚀")

    time.sleep(5)