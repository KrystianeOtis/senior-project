import cv2
import sys
import time
import datetime
import playsound

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

frame_width = int(source.get(3))
frame_height = int(source.get(4))

win_name = 'Data Collection'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
out_mp4 = cv2.VideoWriter(f'{datetime.datetime.now()}.mp4',cv2.VideoWriter_fourcc(*'XVID'), cv2.CAP_PROP_FPS, (frame_width,frame_height))

start_time = time.time()

while cv2.waitKey(1) != 27 and time.time() - start_time <= 15: # Escape
    
    has_frame, frame = source.read()
    if not has_frame:
        break

    out_mp4.write(frame)
    if (time.time() - start_time == 10):
        playsound()

source.release()
cv2.destroyWindow(win_name)