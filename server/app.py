import os
import cv2
import numpy as np
from datetime import datetime
from flask import Flask, request, make_response, render_template
file_path = './static'
app = Flask('__name__')

@app.route('/upload', methods=['POST'])
def upload():
    image_byte = request.data
    image_np = np.frombuffer(image_byte, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    cv2.imwrite(file_path + '/' + timestamp + '.jpg', image)
    return ''

@app.route('/updata', methods=['POST'])
def updata():
    face_cascade = cv2.CascadeClassifier(
            'C:\\Users\\723brian\\Desktop\\face-api\\'
            +'client\\haarcascade_frontalface_default.xml')
    image_byte = request.data
    name = request.args.get('name')
    print(name)
    image_np = np.frombuffer(image_byte, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        image = image[x:x+w, y:y+h]
    cv2.imwrite(name+ '.jpg', image)
    return ''
@app.route('/', methods=['GET'])
def index():
    return 'Hello world'

if __name__ == "__main__":
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    app.run(host='0.0.0.0', debug=False)