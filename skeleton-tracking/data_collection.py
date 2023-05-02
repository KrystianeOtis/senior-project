import cv2
import sys
import time
import datetime
from playsound import playsound




s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

frame_width = int(source.get(3))
frame_height = int(source.get(4))

out_mp4 = cv2.VideoWriter(f'{time.strftime("%Y%m%d-%H%M%S")}.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width,frame_height))

start_time = time.time()

win_name = 'Data Collection'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
# C:/Users/kryst/Documents/School/senior-project/assets/beep-beep.mp3
# C:/Users/mosia/OneDrive/Desktop/Senior Project/senior-project/assets/beep-beep.mp3
playsound('C:/Users/kryst/Documents/School/senior-project/assets/beep-beep.mp3')

while cv2.waitKey(1) != 27 and time.time() - start_time <= 15: # Escape

    has_frame, frame = source.read()
    if not has_frame:
        break

    cv2.imshow(win_name, frame)

    out_mp4.write(frame)
    if (int(time.time() - start_time) == 10):
        # C:/Users/kryst/Documents/School/senior-project/assets/beep-beep.mp3
        # C:/Users/mosia/OneDrive/Desktop/Senior Project/senior-project/assets/beep-beep.mp3
        playsound('C:/Users/kryst/Documents/School/senior-project/assets/beep-beep.mp3')

source.release()