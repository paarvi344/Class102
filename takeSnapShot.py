import cv2

def take_snapshot():
    # inititializing camera i.e cv2

    videocaptureObject = cv2.VideoCapture(0)
    result = True 
    while (result) :

     #reading the frame while camera is on
        ret,frame = videocaptureObject.read()

     #cv2.im write is a method to save an image to any storage  device
        cv2.imwrite("NewPicture1.jpg",frame)
        result= False

# releases the camera 
    videocaptureObject.release()

#closes all the window that might be opened during the process
    cv2.destroyAllWindows()


take_snapshot()


