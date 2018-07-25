import cv2
import socket

host = "localhost"
port = 4096
addr = (host, port)

cap = cv2.VideoCapture(0)

FPS = cap.get(cv2.CAP_PROP_FPS)
setFPS = 15
ratio = int(FPS) / setFPS
count = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            count = count + 1
            if count == ratio:
                encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
                result, encoded_img = cv2.imencode('.jpg', frame, encode_param)
                if not result:
                    break
                sock.sendto(encoded_img.tobytes(), addr)
                count = 0
        else:
            break
except KeyboardInterrupt:
    cap.release()
    sock.close()

cap.release()
sock.close()
