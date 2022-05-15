import cv2
print(cv2.__version__)


cam = cv2.VideoCapture(0)

cam.set(3, 640) # 3 is the width of the frame
cam.set(4, 480) #

x = 0
y = 0
dx = 1
dy = 2

while True:
    success, frame = cam.read()

    cv2.putText(frame, "MBS3523 Assignment 1b - Q3 Name: Yeung Yin Hang Herny", (40, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 207, 13), 2)
    cv2.rectangle(frame, (x, y), (x + 80, y+80), (124, 252, 124), 2)
    x = x + dx
    if x >= 560 or x <= 0:
        dx = dx * (-1)

    y = y + dy
    if y >= 400 or y <= 0:
        dy = dy * (-1)

    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()