from PIL import Image
import cv2
import numpy as np

def grayscale(image_bytes):

    np_array = np.frombuffer(image_bytes, np.uint8)

    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, buffer = cv2.imencode(".png", gray)

    return buffer.tobytes()