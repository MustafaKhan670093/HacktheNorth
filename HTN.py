from clarifai import rest
from clarifai.rest import ClarifaiApp
import clarifai
import cv2
import os
import sys
import requests
import firebase_admin
from firebase_admin import credentials, storage, firestore
from picamera import PiCamera
from time import sleep
from ipstack import GeoLookup






cred = credentials.Certificate('potholer-hackthenorth-firebase-adminsdk-tpuya-d3e3dda5a3.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://potholer-hackthenorth.appspot.com/'
})
bucket = storage.bucket('potholer-hackthenorth.appspot.com')
db = firestore.client()
x = 0
camera = PiCamera()
sleep(5)

while True:
    camera.start_preview()
    camera.capture('/home/pi/Desktop/binny/test.jpg')

    app = ClarifaiApp(api_key='fe05f44aa9304a629963060db88c9550')
    model = app.models.get("potholedetect")

    response = model.predict_by_filename("test.jpg")

    response = str(response)
    for i in range(len(response)):
        if response[i] == "0" and response[i+1] == ".":
            answer = response[i:i+3]
            if float(answer) >= 0.7:
                print("found")
                x = x+1
                geo_lookup = GeoLookup("367b4e6fe41e712cfd85feb52af4cb11")
                location = geo_lookup.get_own_location()
                print(location.get('latitude'))
                print(location.get('longitude'))
                data = {
                    u'imageid' : "pothole" + str(x),
                    u'location': [location.get('latitude'), location.get('longitude')]
                }
                db.collection(u'pothole_details').document(u'pothole' + str(x)).set(data)
                blob = bucket.blob("pothole" + str(x))
                blob.upload_from_filename("test.jpg")


