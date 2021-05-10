# Invisibility_Cloak
For all the Harry Potter and SiFi fan!! Now you can finally go completely INVISABLEQ !! Utilizing the power of OpenCV and python 

**Final Output Below :)**

***Input***
* Initial frame
  * Background
* Live Video Frame

***Output***
* Harry's Invisable Cloak  

# Pseudocode
1) Capture an Initial frame, this will be the background
2) Capture Live Video. 
3) Optimize it for processing: *Convert **BGR to HSV , Apply GaussianBlur**
4) Calcualte *HVS values of the Cloak*
5) Create a **mask** of the ROI(cloak)
6) Inverse the mask utlizing cv2.Threshold type cv.THRESH_BINARY_INV
7) Apply cv2.bitwise_and operation onto the frames
    *   LiveFrame = **cv.bitwise_and**(maskInv, frame)
        *   This will **remove the ROI**(cloak) area from the live frame. 
    *   cloakArea = cv.bitwise_and(frameINT, mask)
        *   This will **remove all non ROI**(cloak) area from the Initial frame.
8) Apply cv2.bitwise_OR operation onto the frames
    *   FinalFrame = **cv.bitwise_or**(LiveFrame, cloakArea)
        *   This will mask the frames togeather.
# FINAL OUTPUT
https://user-images.githubusercontent.com/83566027/117606118-d7389900-b176-11eb-8693-65f8fea39eb1.mp4

# DONE
