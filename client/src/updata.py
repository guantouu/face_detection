import cv2
import requests
import json

if __name__ == "__main__":
    name = input("input file name:")
    frame = cv2.imread('./picture/' + name + '.png')
    _, frame_encode = cv2.imencode('.jpg', frame)
    r = requests.post('http://127.0.0.1:5000/updata?name=' + name, data=frame_encode.tostring())
