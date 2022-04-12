
import firebase_admin
from firebase_admin import credentials

def initializeFirebase():
    cred = credentials.Certificate("fedstation-firebase-firebase-adminsdk-gp3fm-d691bf3872.json")
    firebase_app  = firebase_admin.initialize_app(cred , {
        "databaseURL" : "https://fedstation-firebase.firebaseio.com", 
        "storageBucket":"fedstation-firebase.appspot.com"
    } )
    print(firebase_app.name , "Firebase Initialized")