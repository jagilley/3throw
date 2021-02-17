#import RPi.GPIO as GPIO
from flask import Flask, render_template, request, Response
import json
app = Flask(__name__)
import cv2
import sys
import math
import logging as log
import datetime as dt
from time import sleep
import argparse
import serial


ser = serial.Serial('/dev/ttyACM0', 9600)
instructions = {'a', 's', 'd' ,'w', 'k', 'r'}
parser = argparse.ArgumentParser()
parser.add_argument("ml", type=str)
args = parser.parse_args()

if args.ml == "True" or args.ml == "true":
   print("Performing facial recognition")
   ml = True
else:
   ml = False
   print("Not doing facial recognition")

video_cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
anterior = 0

#GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : "GPIO.LOW"},
   24 : {'name' : 'GPIO 24', 'state' : "GPIO.LOW"}
   }


@app.route("/")
def main():
   return render_template('webserver.html')

#generator() and video_feed are a pair of function that handles the video streaming
def generator():
   while True:
      if not video_cap.isOpened():
         raise RuntimeError('camera not started')
      _, frame = video_cap.read()
      
      if ml:
         #facial recognization
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #opencv color converter
         faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.1,
         minNeighbors=5,
         minSize=(20, 20)
         )

         for (x, y, w, h) in faces:
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (x + int(w/2), y + int(h/2)), int(math.sqrt(w*w+h*h)/2), (0, 255, 0), 2)
            cv2.line(frame, (x,y),(x+w, y+h), (0, 0, 255), 2)
            cv2.line(frame, (x + w,y), (x, y + h), (0, 0, 255), 2 )

      # if anterior != len(faces):
      #    anterior = len(faces)
      #    log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))"""

      #frame.shape = 480 (height) * 640 (width) *3 (BGR)
      # draw telescope 
      center_x = 320
      center_y = 240
      Out_r = 25
      in_r = 6
      cv2.circle(frame, (center_x, center_y), Out_r, (0, 0, 0), 2)
      cv2.line(frame, (center_x, center_y - Out_r), (center_x, center_y - in_r), (0, 0, 0), 1)
      cv2.line(frame, (center_x, center_y + Out_r), (center_x, center_y + in_r), (0, 0, 0), 1)
      cv2.line(frame, (center_x - Out_r, center_y), (center_x - in_r, center_y), (0, 0, 0), 1)
      cv2.line(frame, (center_x + Out_r, center_y), (center_x + in_r, center_y), (0, 0, 0), 1)

      result = cv2.imencode('.jpg', frame)[1].tobytes()


      yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + result + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
   return Response(generator(),
                     mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/postmethod",methods = ['POST'])
def parseJSdata():
   key = request.form['keyboard']
   if(key in instructions):
      ser.write(key.encode())
      print("instruction " + key + " sent")
   
   # if(key == )
   # if(key == 'a'):
   #    print('left')
   # elif(key == 's'):
   #    print('down')
   # elif(key == 'w'):
   #    print('up')
   # elif(key == 'd'):
   #    print('right')
   # elif(key == 'k'):
   #    print("accumulating power")
   # elif(key == 'r'):
   #    print("shoot!")

   return "return"
   

if __name__ == "__main__":
    # send request to http://10.106.2.85:5000
    app.run(host='0.0.0.0')