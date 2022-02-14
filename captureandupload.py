import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    # inititializing camera i.e cv2

    number = random.randint(0,100)

    videocaptureObject = cv2.VideoCapture(0)
    result = True 
    while (result) :

     #reading the frame while camera is on
        ret,frame = videocaptureObject.read()

     #cv2.im write is a method to save an image to any storage  device
        img_name = "img"+str(number)+".png"

        cv2.imwrite(img_name,frame)
        start_time = time.time
        result= False

# releases the camera 
    return img_name
    print("snapShots taken")
    videocaptureObject.release()

#closes all the window that might be opened during the process
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN"

    file = img_name
    file_from = file
    file_to = "/TestFolder/"+(img_name)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f :
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("Files Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)


main()


