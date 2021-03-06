from imutils.video.pivideostream import PiVideoStream
import time
import simplejpeg as sj


print("[INFO] Start 'simplejpeg' benchmark")
vs = PiVideoStream(resolution=(1280,640)).start()
time.sleep(1.0)

frameCount = 0
timePoint = time.time()
while (time.time()-timePoint<10):
    # frame = vs.read()
    buffer = sj.encode_jpeg(vs.read(),30,'rgb','444',True)
    frameCount += 1

print("{:.2f}\n{:.2f}".format(frameCount/(time.time()-timePoint),time.time()-timePoint))
vs.stop()

