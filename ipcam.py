import cv2
import numpy as np
import imutils
import requests
import os

url = "http://192.168.0.105:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)

    cv2.imshow('IpCam', img)
    cv2.waitKey(1)
    c = cv2.waitKey(1)
    if c == 27 or c == 10:
        cv2.destroyAllWindows()
        cap.release()
        break