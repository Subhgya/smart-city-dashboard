from flask import Flask, jsonify
from flask_cors import CORS
from firebase_config import db, firebase_available

app = Flask(__name__)
CORS(app)

def get_data(collection):
    if not firebase_available or db is None:
        return []
    docs = db.collection(collection).order_by("timestamp").limit(24).stream()
    return [doc.to_dict() for doc in docs]

@app.route("/traffic")
def traffic():
    return jsonify(get_data("traffic"))

@app.route("/pollution")
def pollution():
    return jsonify(get_data("pollution"))

@app.route("/energy")
def energy():
    return jsonify(get_data("energy"))

@app.route("/waste")
def waste():
    return jsonify(get_data("waste"))

if __name__ == "__main__":
    app.run(debug=True)