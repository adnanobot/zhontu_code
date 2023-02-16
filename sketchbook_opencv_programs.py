import cv2
import numpy as np
import time


def overlapping_boxes():
    height = 300
    width = 300

    image = np.zeros((height, width, 3), np.uint8)

    image[100:200, 100:200] = (255, 0, 255)
    image[150:250, 150:250] = (0, 0, 255)

    alpha = 0.5
    beta = 0.9

    # show circle 3 sec
    # with box
    # do not show for 0.5 sec
    # 5 sec without box
    # box .... no box  .... 5 sec .... box again
    image = np.zeros((height, width, 3), np.uint8)
    counter = 0
    while True:
        image[100:200, 100:200] = (255, 0, 255)
        image[150:250, 150:250] = (0, 0, 255)

        circle_bg = np.zeros((300, 300, 3), np.uint8)
        circle = cv2.circle(circle_bg, (150, 150), 100, (50, 50, 200), -1)
        cv2.addWeighted(circle, alpha, image, beta, 0.0, image)
        cv2.imshow("image", image)
        cv2.waitKey(0)
        # time.sleep(2)

        image = np.zeros((height, width, 3), np.uint8)
        image[100:200, 100:200] = (255, 0, 255)
        image[150:250, 150:250] = (0, 0, 255)
        cv2.imshow("image", image)
        cv2.waitKey(0)
        # time.sleep(2)

        print(counter)
        counter = counter + 1
        if counter == 2000:
            break

    cv2.destroyAllWindows()


def draw_moving_circle():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow("frame", frame)

        key = cv2.waitKey(0)
        if key == ord("q"):
            break

if __name__ == '__main__':
    draw_moving_circle()

