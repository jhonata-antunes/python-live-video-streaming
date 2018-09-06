# Python live video streaming
This example shows how to send and receive live video streaming, using UDP protocol. Frames are captured using OpenCV. Each frame is compressed, using JPEG, decreasing quality until frame size is less than 65 KB, according to UDP socket restriction.
## Setup
1. Install OpenCV library `$ sudo apt-get install libopencv-dev python-opencv`
2. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
3. Activate virtualenv `$ source venv/bin/activate`
4. Install requirements `$ pip install -r requirements.txt`
## Usage
- Run `$ python3 client.py`, that will capture images from file or WebCam (`Ctrl+C` to exit)
  - `--video VIDEO` Path to video file (default value: WebCam)
  - `--fps FPS` Video FPS (default value: 14)
  - `--gray` Convert video into gray scale (default value: `None`)
  - `--ip IP` Server IP address (default value: localhost)
  - `--port PORT` UDP port number (default value: 60444)
- Run `$ python3 server.py`, that will receive frames from client and display or save, using OpenCV (`q` if the window is displayed, else `Ctrl+C` to exit)
  - `--save` Save video (default value: `None`)
  - `--ip IP` Server IP address (default value: localhost)
  - `--port PORT` UDP port number (default value: 60444)
## References
- [UDP Communication](https://wiki.python.org/moin/UdpCommunication)
- [yushuhuang/webcam](https://github.com/yushuhuang/webcam/blob/master/send/captureSend.py)
- [OpenCV and IP camera streaming with Python](http://benhowell.github.io/guide/2015/03/09/opencv-and-web-cam-streaming)