import cv2
import mediapipe as mp

cam = cv2.VideoCapture("mrBean.mp4")

width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

faces = mp.solutions.face_detection.FaceDetection()
while True:
    _ , frame = cam.read() # reading one frame from the camera object
    if _: # if frame received proceed
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) # Convert to
       
        faceResults = faces.process(frameRGB) # this returns list of
    
        if faceResults.detections != None: # if detection is non
    
            for face in faceResults.detections: # iterate through
     
                bBox = face.location_data.relative_bounding_box #
    
    # splitting into variables and converting to
    
            x =int(bBox.xmin*width)
            y=int(bBox.ymin*height)
            w=int(bBox.width*width)
            h=int(bBox.height*height)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('Webcam', frame)
     # Waits for 1ms and check for the pressed key
    if cv2.waitKey(1) & 0xff == ord('q'): # press q to quit the camera
     break
cam.release() # close the camera
cv2.destroyAllWindows() # Close all the active windows