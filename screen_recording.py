import cv2
import numpy as np
import time
from win32api import GetSystemMetrics
import pyautogui

width=GetSystemMetrics(0)  #for taking current screen size. no need to specify 1080 *720
height=GetSystemMetrics(1)
dim=(width,height)



format = cv2.VideoWriter_fourcc(*"XVID")
# XVID this contain video all format like mp4,hd

# Specify name of Output file
filename = "recording.mp4"

fps=60

# Creating a VideoWriter object
output = cv2.VideoWriter(filename,format, fps,dim)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
  
# Resize this window
cv2.resizeWindow("Live", 480, 270)



while True:
  
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
  
    # Convert the screenshot to a numpy array
    frame = np.array(img)
  
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
    # Write it to the output file
    output.write(frame)
      
    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
        
        
        
        
# Release the Video writer
output.release()
  
# Destroy all windows
cv2.destroyAllWindows()
