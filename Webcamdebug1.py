import numpy as np
import cv2
 cap = cv2.VideoCapture(0)

 while(True):
     #Capture the damn VideoCapture
     ret, frame = cap.read()

     #operations on frame come where
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     #Dispaly the result where
     cv2.waitKey(1) & 0xFF == ord ('q');
     break

#when everythinbg is done
cap.release()
cv2.destroyAllWindows() 
