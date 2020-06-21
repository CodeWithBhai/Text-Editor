import cv2

face_cascade = cv2.CascadeClassifier('cascade.xml')

eye_cascade = cv2.CascadeClassifier('cascade.xml')

#capture frame from camera
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #face detect different size
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        gray1 = gray[y : y+h, x : x+w]
        color = img[y:y+h, x: x+w]

        #detect eye
        eye = eye_cascade.detectMultiScale(gray1)

        #draw rec for eye
        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(color, (ex, ey), (ex + eh, ey +eh), (0, 127, 255), 2)


            #display image
            cv2.imshow('img', img)

            #waiting for esc

            p = cv2.waitKey(30) & 0xff
            if p == 27:
                break

                #close window

                cap.release()
                cv2.destoryAllWindows()