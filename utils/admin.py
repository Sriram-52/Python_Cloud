import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("utils/admin.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
