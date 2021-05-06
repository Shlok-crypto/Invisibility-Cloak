import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

outVideo = cv.VideoWriter( 'invisible4.mp4', -1, 20.0, (640,480) )


def temps(x):
    pass

# Creating Trackbar Window
# Default color ark blue(109,101,142,98,125,2)
# light pink (180,102,59,7,237,119)
# Maroon (180,151,255,118,255,0)
bars = cv.namedWindow("bars")
cv.createTrackbar("up_hue","bars", 180, 180, temps)
cv.createTrackbar("low_hue","bars", 151, 180, temps)
cv.createTrackbar("up_saturation","bars", 255, 255, temps)
cv.createTrackbar("low_saturation","bars", 118, 255, temps)
cv.createTrackbar("up_value","bars", 255, 255, temps)
cv.createTrackbar("low_value","bars", 0, 225, temps)
cv.createTrackbar("thresh","bars", 0, 225, temps)

# Capturing the initial frame
_,frameINT = capture.read()

while True:
    _, frame = capture.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# Getting the HSV values for masking the cloak
    upper_hue = cv.getTrackbarPos("up_hue", "bars")
    upper_saturation = cv.getTrackbarPos("up_saturation", "bars")
    upper_value = cv.getTrackbarPos("up_value", "bars")
    lower_value = cv.getTrackbarPos("low_value", "bars")
    lower_hue = cv.getTrackbarPos("low_hue", "bars")
    lower_saturation = cv.getTrackbarPos("low_saturation", "bars")
    threshh = cv.getTrackbarPos("thresh","bars")

# HSV values of ROI
    lower_hsv = np.array([lower_hue, lower_saturation, lower_value])
    upper_hsv = np.array([upper_hue, upper_saturation, upper_value])

# Creating mask of the ROI
    mask = cv.inRange(frame_hsv, lower_hsv, upper_hsv)
    blur = cv.GaussianBlur(frame,(7,7),0)

# Make the Roi Black
    mask = cv.dilate(mask,None,iterations=7)
    _, maskInv = cv.threshold(mask, 0, 255, cv.THRESH_BINARY_INV) # [pixel>127 => black(0)] & [pixel<127 => white(255)]

    # Convert masks(gray) to BGR (2 Channel to 3 Channel )
    maskInv = cv.cvtColor(maskInv, cv.COLOR_GRAY2BGR)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

# Combining the frames togeather
# Taking the negative of each frame
    frame_inv = cv.bitwise_and(maskInv, frame)
    cloakArea = cv.bitwise_and(frameINT, mask)

# Combining both of the frames
    final = cv.bitwise_or(frame_inv, cloakArea)

    outVideo.write(final)
    cv.imshow("Invisible Cloak", final)
    #cv.imshow("dilation",maskInv)
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
outVideo.release()
cv.destroyAllWindows()