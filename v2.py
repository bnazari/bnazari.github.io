import cv2
import os
import numpy as np

import sys
filename = sys.argv[1]
image_filename=os.path.splitext(filename)[0]
os.mkdir(image_filename) 
cam = cv2.VideoCapture(filename)
length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
print("Reading movie from: "+ filename)
print("Total number of frames: "+ str(length))
frames_skip=length/201
print("Saving a frame roughly everything " +str(round(frames_skip,1)) + " frames.")
original_frameno = 0
next_save_frameno=0
current_frameno=0
while(True):
	ret,frame = cam.read()
	if ret: 
		if original_frameno==int(next_save_frameno):
			cv2.imwrite("%s/%s.%d.jpg" % (image_filename,image_filename,current_frameno), frame)
			next_save_frameno = next_save_frameno + frames_skip
			current_frameno=current_frameno+1
		original_frameno += 1
	else:
		break
cam.release()
cv2.destroyAllWindows()
