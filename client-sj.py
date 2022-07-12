from imutils.video.pivideostream import PiVideoStream
import time
import socket,pickle,os
import simplejpeg as sj

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,1000000)
server_ip = "192.168.101.6"
server_port = 6666

print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream(resolution=(800,640)).start()
time.sleep(1.0)
while True:
    s.sendto((pickle.dumps(sj.encode_jpeg(vs.read(),30,'rgb','444',True))),(server_ip,server_port))
vs.stop()

