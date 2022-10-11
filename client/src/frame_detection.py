import cv2
import time
import threading
import requests
import multiprocessing as mp
URL = 'http://flask.guantouu.pw/upload'

class FrameDetection():
    def face_detection(self, face_queues, location_queues):
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        while True :
            if face_queues.empty() == True:
                time.sleep(0.01)
                continue
            frame = face_queues.get()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
            for (x, y, w, h) in faces:
                square_point = [x, y, w, h]
                location_queues.put(square_point)
                location_queues.get() if location_queues.qsize() > 1 else time.sleep(0.01)
                t = threading.Thread(target=self.upload_detection, args=(frame,))
                t.start()
                time.sleep(1)
            
                

    def upload_detection(self, frame):
        _, frame_encode = cv2.imencode('.jpg', frame)
        r = requests.post('http://127.0.0.1:5000/upload', data=frame_encode.tostring())