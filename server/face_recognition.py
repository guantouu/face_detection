import cv2
import os
import numpy as np
path = 'C:\\Users\\723brian\\Desktop\\face-api\\server\\rec'

def read_images(path, sz=None):
    c = 0 
    x, y, name = [], [], []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            name.append(filename)
            im = cv2.imread(os. path.join(dirname,filename),
                                      cv2.IMREAD_GRAYSCALE)
            im = cv2.resize(im, (200, 200))
            while True:
                cv2.imshow('display', im)
                if cv2.waitKey(1) == 27:
                    cv2.destroyAllWindows()
                    break
            x.append(np.asarray(im, dtype=np.int8))
            y.append(c)
            c = c + 1  
    return [x, y], name

def face_rec(frame, x, y, name):
    face_cascade = cv2.CascadeClassifier(
            "C:\\Users\\723brian\\Desktop\\face-api\\"
            + "client\\haarcascade_frontalface_default.xml")
    model =cv2.face.EigenFaceRecognizer_create()
    model.train(np.asarray(x), np.asarray(y))
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        roi = gray[x:x+w, y:y+h]
        roi = cv2.resize(roi, (200, 200), cv2.INTER_LINEAR)
        while True:
            cv2.imshow('display', roi)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break
        params = model.predict(roi)
        print(params[0], params[1])

[x, y], name = read_images(path)
frame = cv2.imread('C:\\Users\\723brian\\Desktop\\face-api\\server\\momo.png')
face_rec(frame, x, y, name)
