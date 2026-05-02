import os

try:
    import firebase_admin
    from firebase_admin import credentials, firestore

    # Check if service account key exists
    key_path = "../serviceAccountKey.json"
    if os.path.exists(key_path):
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        firebase_available = True
        print("Firebase initialized in backend ✅")
    else:
        firebase_available = False
        db = None
        print("Firebase service account key not found. Backend will not function.")
except ImportError:
    firebase_available = False
    db = None
    print("Firebase not installed. Backend will not function.")