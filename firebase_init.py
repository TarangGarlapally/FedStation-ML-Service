
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def initializeFirebase():
    cred = credentials.Certificate("fedstation-firebase-firebase-adminsdk-gp3fm-d691bf3872.json")
    firebase_app  = firebase_admin.initialize_app(cred , {
        "databaseURL" : "https://fedstation-firebase.firebaseio.com"
    } )
    print(firebase_app.name , "Firebase Initialized")
    
    db = firestore.client() 
    docs  = db.collection("dumy").get()
    for doc in docs:
        print(doc.to_dict())