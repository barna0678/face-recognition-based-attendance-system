import cv2
import os
import csv
import time
from datetime import datetime 

from win32com.client import Dispatch

speaker = Dispatch("SAPI.SpVoice")

video = cv2.VideoCapture(0)

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer.yml')

name_list = ["","Barna","Dia","Mrinalini"]

COL_NAME=["ID","NAME","DATE","TIME"]

while True:

    ret,frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        serialnumber,confidence = recognizer.predict(gray[y:y+h,x:x+w])

        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        timestamp=datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        attendance = [str(serialnumber),str(name_list[serialnumber]),str(date),str(timestamp)]
        

        if confidence < 50:
          print("Recognized person: "+ name_list[serialnumber] + " with confidence: "+ str(confidence))
          cv2.putText(frame,name_list[serialnumber],(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)

          exist=os.path.isfile("Attendance/Attendance_"+ date +".csv")

          #k=cv2.waitKey(1)
          #if k==ord('a'):

          if not exist:
              with open('Attendance/Attendance_'+ date +'.csv','a+') as csvFile:
                writer=csv.writer(csvFile)
                writer.writerow(COL_NAME)
                writer.writerow(attendance)
              csvFile.close()
          else:
              with open('Attendance/Attendance_'+ date +'.csv','a+') as csvFile:
                writer=csv.writer(csvFile)
                writer.writerow(attendance)
              csvFile.close()

          speaker.Speak("Attendance taken for "+ name_list[serialnumber])
          time.sleep(5)
            
        else:
          print("Unknown face detected")
          cv2.putText(frame,"Unknown",(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)

          #speaker.Speak(" unknown face detected ")
          #time.sleep(5)
        
    cv2.imshow('frame',frame)

    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("Face recognition process ended, attendance taken...")