import cv2, time

print("[INFO] Start 'OpenCV' benchmark")
cap = cv2.VideoCapture(0)
time.sleep(1.0)

frameCount = 0
timePoint = time.time()
while (time.time()-timePoint<10):
    succ, img = cap.read()
    frameCount += 1

print("{:.2f}\n{:.2f}".format(frameCount/(time.time()-timePoint),time.time()-timePoint))
cap.release()