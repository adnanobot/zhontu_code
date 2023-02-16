import cv2
import numpy as np

def put_pt_on_frame(point, color):
    return cv2.circle(frame, point, 3, color, -1)

height = int(1200)
width = int(1920)

frame = np.zeros((height, width, 3), np.uint8)
frame[:, :] = (55, 5, 55)

fblx = 638
fbly = 355
fbrx = 658
fbry = 355
ftlx = 638
ftly = 282
ftrx = 658
ftry = 282
bblx = 652
bbly = 352
bbrx = 670
bbry = 352
btlx = 652
btly = 278
btrx = 670
btry = 278

cube = [(fblx, fbly), (fbrx, fbry), (ftlx, ftly), (ftrx, ftry), (bblx, bbly), (bbrx, bbry), (btlx, btly), (btrx, btry)]

for point in cube:
    frame = put_pt_on_frame(point, (55, 0, 255))

cv2.line(frame, (fblx, fbly), (fbrx, fbry), (255, 0, 255), 1)
cv2.line(frame, (fblx, fbly), (ftlx, ftry), (255, 0, 255), 1)
cv2.line(frame, (fbrx, fbry), (ftrx, ftry), (255, 0, 255), 1)
cv2.line(frame, (ftlx, ftly), (ftrx, ftry), (255, 0, 255), 1)

cv2.line(frame, (bblx, bbly), (bbrx, bbry), (55, 255, 55), 1)
cv2.line(frame, (bblx, bbly), (btlx, btry), (55, 255, 55), 1)
cv2.line(frame, (bbrx, bbry), (btrx, btry), (55, 255, 55), 1)
cv2.line(frame, (btlx, btly), (btrx, btry), (55, 255, 55), 1)

cv2.line(frame, (fblx, fbly), (bblx, bbly), (255, 255, 255), 1)
cv2.line(frame, (fbrx, fbry), (bbrx, bbry), (255, 255, 255), 1)
cv2.line(frame, (ftlx, ftly), (btlx, btly), (255, 255, 255), 1)
cv2.line(frame, (ftrx, ftry), (btrx, btry), (255, 255, 255), 1)


cv2.imshow("frame", frame)
cv2.waitKey(0)