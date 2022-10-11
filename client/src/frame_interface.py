import cv2
import time
import multiprocessing as mp

class FrameInterface():
    def entrance(self, face_queues, output_queues):
        cap = cv2.VideoCapture(0)
        while True :
            ret, frame = cap.read()
            face_queues.put(frame)
            output_queues.put(frame)
            face_queues.get() if face_queues.qsize() > 1 else time.sleep(0.01)
            output_queues.get() if output_queues.qsize() > 1 else time.sleep(0.01)
        cap.release()
            
    def output(self, output_queues, location_queues):
        while True :
            frame = output_queues.get()
            if location_queues.empty() == False:
                square_point = location_queues.get()
                cv2.rectangle(frame, (square_point[0], square_point[1]),
                                     (square_point[0] + square_point[2],
                                      square_point[1] + square_point[3]),
                                     (0,255,0), 4, cv2.LINE_AA)
            cv2.imshow('display', frame)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break