import multiprocessing as mp
from frame_interface import FrameInterface
from frame_detection import FrameDetection

class MainProcess():
    def __init__(self):
        self.frame_detection = FrameDetection()
        self.frame_interface = FrameInterface()
    
    def process_controller(self):
        face_queues = mp.Queue(maxsize=4)
        location_queues = mp.Queue(maxsize=4)
        output_queues = mp.Queue(maxsize=4)
        entrance = mp.Process(
            target=self.frame_interface.entrance, 
            args=(face_queues, output_queues)
            )
        output = mp.Process(
            target=self.frame_interface.output,  
            args=(output_queues, location_queues)
            )
        face_detection = mp.Process(
            target=self.frame_detection.face_detection,  
            args=(face_queues, location_queues)
            )
        entrance.start()
        output.start()
        face_detection.start()
        while True :
            if output.is_alive() is False:
                entrance.terminate()
                face_detection.terminate()
                break

        
if __name__ == '__main__':
    main = MainProcess()
    main.process_controller()
    