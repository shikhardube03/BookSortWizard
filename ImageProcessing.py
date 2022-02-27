import pytesseract as tess
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from IPython.display import display
from pytesseract import image_to_string
from PIL import Image


# tesseract --help-extra or tesseract --help-psm to find info about the segmentation modes

file = "TestImages/Label2.png"
img = Image.open(file)

# grayscale image
# img = img.convert('L') 

# OpenCV and Matplot rendering of file
white = cv2.imread(file)
gray = cv2.cvtColor(white, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# gets OCR data as string from passed image
data = tess.image_to_string(img, lang = 'eng',config='--psm 1')

all_lines = data.splitlines()
print(all_lines)
print('\n')

def group_lines_into_books(sequence, separator):
    book = []
    for elem in sequence:
        if elem == separator:
            yield book
            book = []
        book.append(elem)
    yield book

result = list(group_lines_into_books(all_lines, ''))

def remove_empty_strings(sequence):
	new_book_list = list()
	for little_list in sequence:
		if isinstance(little_list, list):
			new = list()
			for elem in little_list:
				if elem != '':
					new.append(elem)
			if len(new) == 0:
				continue
		elif isinstance(little_list, str):
			if little_list == '':
				continue
			new = little_list
		else:
			new = little_list
		new_book_list.append(new)
	return new_book_list
    

result = remove_empty_strings(result)
print(result)


