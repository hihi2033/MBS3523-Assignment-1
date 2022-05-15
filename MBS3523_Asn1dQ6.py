import cv2

EVT = 0

def draw_rectangle(event,x,y,flags,param):
    global EVT
    global PNT1
    global PNT2
    if event == cv2.EVENT_LBUTTONDOWN:
        EVT = event
        PNT1 = (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        EVT = event
        PNT2 = (x, y)
    if event == cv2.EVENT_RBUTTONUP:
        EVT = event

cv2.namedWindow('MBS3523')
cv2.setMouseCallback('MBS3523',draw_rectangle)

cam = cv2.VideoCapture(0)


while True:
    _, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1b-Q6 Name: Ho Chun Yip', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 255), 2)

    if EVT == 4:
        cv2.rectangle(img, PNT1, PNT2, (255,0,255), 3)
        imgROI = img[PNT1[1]:PNT2[1], PNT1[0]:PNT2[0]]
        cv2.imshow('ROI', imgROI)
    if EVT == 5:
        img[:,:] = img
        cv2.destroyWindow('ROI')
        EVT = 0

    cv2.imshow('MBS3523', img)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()