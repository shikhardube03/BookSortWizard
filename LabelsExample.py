import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import pytesseract
from ProcessImage import get_labels

  labels4 = get_labels("Books4.jpeg", thresh=190)
   for x in sorted(labels4.keys()):
      cv2.imshow(str(x), labels4[x])
      print("Key: " + str(x))
      print(pytesseract.image_to_string(labels4[x], lang='eng', config="--psm 6"))
   cv2.waitKey(0)
   cv2.destroyAllWindows()
