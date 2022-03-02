import pyrebase

config = {
    "apiKey": "AIzaSyCf6ey3i7IVAaaY9oJN_qyav8CTxcXibIA",
    "authDomain": "social-geeks-6a937.firebaseapp.com",
    "projectId": "social-geeks-6a937",
    "databaseURL": "https://social-geeks-6a937-default-rtdb.firebaseio.com/",
    "storageBucket": "social-geeks-6a937.appspot.com",
    "messagingSenderId": "202105473081",
    "appId": "1:202105473081:web:64c816220f4b5d8f35a5e8",
    "measurementId": "G-M94K6FRGTB"
}

firebase_config = pyrebase.initialize_app(config)

database = firebase_config.database()