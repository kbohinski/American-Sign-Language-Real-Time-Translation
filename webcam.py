import cv2
from sklearn.externals import joblib
import numpy as np


def main():

    roi_rec_cords = ((100, 100), (500, 500))

    cap = cv2.VideoCapture(0)

    counter = 0
    while True:
        ret, frame = cap.read()

        # resizes to correct input
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        x1, x2 = roi_rec_cords[0][0], roi_rec_cords[1][0]
        y1, y2 = roi_rec_cords[0][1], roi_rec_cords[1][1]
        roi_rec = frame[y1:y2, x1:x2]  # numpy switches x and y..

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255))

        counter = counter + 1
        if counter == 11:
            counter = 0
        # cv2.imshow('skin', skin)
        cv2.imshow('frame', frame)

        k = cv2.waitKey(33)
        if k == 27:  # Esc key to stop
            break
        # elif k == -1:
        #     pass
        # else:
        #     print(k)


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()