from clarifai import rest
from clarifai.rest import ClarifaiApp
import clarifai
import cv2
import os
import time
start_time = time.time()


app = ClarifaiApp(api_key='fe05f44aa9304a629963060db88c9550')
model = app.models.get("potholedetect")

response = model.predict_by_filename("test.jpg")

response = str(response)
for i in range(len(response)):
    if response[i] == "0" and response[i+1] == ".":
        answer = response[i:i+3]
        if float(answer) > 0.8:

import sys
import requests
import firebase_admin
from firebase_admin import credentials

from firebase_admin import storage


cred = credentials.Certificate('potholer-hackthenorth-firebase-adminsdk-tpuya-d3e3dda5a3.json')
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://potholer-hackthenorth.appspot.com/'
})


bucket = storage.bucket('potholer-hackthenorth.appspot.com')

blob = bucket.blob("test-blob")
#blob.download_to_filename("potholetest.jpeg")
blob.upload_from_filename("test.jpg")

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/binny/image.jpg')
camera.stop_preview()

from ipstack import GeoLookup
geo_lookup = GeoLookup("367b4e6fe41e712cfd85feb52af4cb11")
location = geo_lookup.get_own_location()
print(location.get('latitude'))
print(location.get('longitude'))
