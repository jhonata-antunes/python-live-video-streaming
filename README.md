# Python live video streaming
This example shows how to send and receive live video streaming, using UDP protocol.
## Setup
1. Install OpenCV library `$ sudo apt-get install libopencv-dev python-opencv`
2. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
3. Activate virtualenv `$ source venv/bin/activate`
4. Install requirements `$ pip install -r requirements.txt`
## Usage
- Run `server.py`, that will capture images from webcam (`Ctrl+C` to exit)
- Run `client.py`, that will receive frames from server and display using OpenCV window (`q` to exit)
## References
- [UDP Communication](https://wiki.python.org/moin/UdpCommunication)
- [yushuhuang/webcam](https://github.com/yushuhuang/webcam/blob/master/send/captureSend.py)
- [OpenCV and IP camera streaming with Python](http://benhowell.github.io/guide/2015/03/09/opencv-and-web-cam-streaming)
