import cv2

video = cv2.VideoCapture(0)

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

id=input('Enter your ID: ')
#id = int(id)
count=0

while True:
    ret,frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        count += 1 #count= count+1
        cv2.imwrite("datasets/user."+str(id)+"."+str(count)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)

    cv2.imshow('frame',frame)

    k=cv2.waitKey(1)

    if count>500:
        break
video.release()
cv2.destroyAllWindows()
print("Data collection completed....")