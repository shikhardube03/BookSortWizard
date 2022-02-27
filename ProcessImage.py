import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

def get_labels(filename, thresh=190):
    image = cv2.imread(filename)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    ret, black = cv2.threshold(gray, 256, 255, cv2.THRESH_BINARY)

    blurred = cv2.GaussianBlur(thresh1, (5, 5), cv2.BORDER_DEFAULT)

    kernel = np.ones((5, 5), np.uint8)

    img_erosion = cv2.erode(blurred, kernel, iterations=1)
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

    tight = cv2.Canny(img_dilation, 240, 250)


    contours, hierarchy = cv2.findContours(tight.copy(), 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    horizontal_to_image = {}

    for i in range(len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        if (w > 50 and h > 50):

            cv2.rectangle(black,(x,y),(x+w,y+h),(255, 255, 255),-1)
            if (len(gray[y:y+h, x:x+w]) > 0):
                while (x in horizontal_to_image.keys()):
                    x+=1
                horizontal_to_image[x] = gray[y:y+h, x:x+w]
    # for key in horizontal_to_image.keys():
    #     cv2.imshow(str(key), horizontal_to_image[key])

    # AND = cv2.bitwise_and(black, gray)
    # cv2.imshow("AND", AND)
    # cv2.imshow("Contours", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return horizontal_to_image

# if __name__ == "__main__":
#     labels = get_labels("Example4.jpeg", thresh=190)
#     for key in labels.keys():
#         cv2.imshow(str(key), labels[key])
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
