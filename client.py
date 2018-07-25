import cv2
import socket

import numpy as np

host = "localhost"
port = 4096
data = b''
buffer_size = 68736

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

try:
    while True:
        data += sock.recv(buffer_size)
        a = data.find(b'\xff\xd8')
        b = data.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = data[a:b + 2]
            data = data[b + 2:]
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('cam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sock.close()

cv2.destroyAllWindows()
sock.close()
