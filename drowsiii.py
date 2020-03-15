import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cam = cv2.VideoCapture(0)
count = 0
countl = 0
countr = 0
avgTl = 0
avgTr = 0
avgl=0
avgr=0
outl = 0
outr = 0
minareal = 10000
minarear = 10000

def noice_reduce(img):
    edges = cv2.Canny(img,100,200)
    kernel = np.ones((2,2),np.uint8)
    #_, thresright = cv2.threshold(rightEye, 42, 255, cv2.THRESH_BINARY_INV)
    img = cv2.dilate(edges,None,iterations=4)
    img = cv2.erode(img,None,iterations=2)
    return img

def cut_eyebrow(img):
    height,width = img.shape[:2]
    eyebrow = height//4
    img = img[eyebrow:height,0:width]
    return img

roiFace = None
area = 0
while True:
    _,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    h,w,_ = frame.shape
    for (x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
     roiFace = frame[y:y+h,x:x+w]
     roiFaceg = gray[y:y+h,x:x+w]
     height,width,_ = roiFace.shape
     eyes = eye_cascade.detectMultiScale(roiFaceg,1.3,5)
     for (x,y,w,h) in eyes:
        if y+h > height/2:
           pass
        cv2.rectangle(roiFace,(x,y),(x+w,y+h),(255,255,0),2)
        eyecenter = x+w/2
        if eyecenter < width/2:
            leftEye = roiFaceg[y:y+h,x:x+w]
            leftEye = cut_eyebrow(leftEye)
            img = noice_reduce(leftEye)
            cv2.imshow("leftarea",img)
            contours,_ = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) != 0:
             cnt = contours[0]
             if len(contours)>1:
              cnt = contours[1]

             area = cv2.contourArea(cnt)
            # print(area,len(contours))
            if area != 0:
                #countl+=1
                avgTl+=area
                countl+=1
                if count>5:
                # print("ads",avgTr//4)
                # print("minarea",minarear)
                 #avgTr=0
                 countl=0
                 if (avgTl//4) < minareal:
                    outl+=1
                   # print("out::",outr)
                    minareal = avgTl//4
                    #print("minarea",minarear)
                    if outl>2:
                        print("wakeup>>>>")
                        outl=0
                 else:
                    outl = 0
                    minareal = avgTl//4
                 avgTl=0
            #cv2.drawContours(leftEye, contours[0] , -1, (0,0,255), 3)
            cv2.imshow("leftEye",leftEye)
        else:
            rightEye = roiFaceg[y:y+h,x:x+w]
            rightEye = cut_eyebrow(rightEye)
            img = noice_reduce(rightEye)
            cv2.imshow("rightarea",img)
            contours,_ = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) != 0:
             cnt = contours[0]
             if len(contours)>1:
              cnt = contours[1]
             area = cv2.contourArea(cnt)
             if area != 0:
                 countr+=1
                 avgTr+=area
                 count+=1
                 if count>5:
                 # print("ads",avgTr//4)
                 # print("minarea",minarear)
                  #avgTr=0
                  count=0
                  if (avgTr//4) < minarear:
                     outr+=1
                    # print("out::",outr)
                     minarear = avgTr//4
                     #print("minarea",minarear)
                     if outr>2:
                         print("wakeup>>>>")
                         outr=0
                  else:
                     outr = 0
                     minarear = avgTr//4
                  avgTr=0

            #cv2.drawContours(rightEye, contours[0] , -1, (0,0,255), 3)
            cv2.imshow("rightEye",rightEye)

    if roiFace is not None :
     cv2.imshow("Show",roiFace)
     if ord('q') == cv2.waitKey(1):
        break
#print("the average isss ::",minarear//count,avgTr//count)
cam.release()
cv2.destroyAllWindows
