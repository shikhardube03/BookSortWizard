from cProfile import label
from curses.ascii import isalnum
from os import remove
from cv2 import setUseOpenVX
import pytesseract as tess
import numpy as np
import cv2
import matplotlib.pyplot as plt
from IPython.display import display
from pytesseract import image_to_string
from PIL import Image
from sympy import sequence
import sorting
import ProcessImage

def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i].compareTo(R[j]) <= 0:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

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
def group_lines_into_books(sequence, separator):
    book = []
    for elem in sequence:
        if elem == separator:
            yield book
            book = []
        book.append(elem)
    yield book

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
			if len(new) > 5:
				new_book_list.append(new)
	return new_book_list
    
def remove_punctuation(sequence):
	# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~-'''
	for i in range(len(sequence)):
		# if sequence[i][3] contains punctuation, remove punctuation
		if sequence[i][2][0] == '-' or sequence[i][2][0] == '.':
			sequence[i][2] = sequence[i][2][1:]
	return sequence

def make_label_list(big_list):
	shelf_list = list()
	for little_list in big_list:
		for elem in little_list:
			if (len(little_list) == 5):
				l1 = sorting.Label(little_list[0], little_list[1], little_list[2],little_list[3], little_list[4])
				shelf_list.append(l1)
			if (len(little_list) == 4):
				l2 = sorting.Label(little_list[0], little_list[1], little_list[2],little_list[3], None)
				shelf_list.append(l2)
			if (len(little_list) == 3):
				l1 = sorting.Label(little_list[0], little_list[1], little_list[2], None, None)
			if (len(little_list) == 2):
				l1 = sorting.Label(None, little_list[1])
				if (isalnum(little_list[0])):
					l1.firstLine = little_list[0]
					l1.secondLine = little_list[1]
					l1.thirdLine = None
					l1.year = None
					l1.version = None
					shelf_list.append(l1)
				else:
					l1.firstLine = None
					l1.secondLine = little_list[2]
					l1.thirdLine = None
					l1.year = None
					l1.version = None
					shelf_list.append(l1)
	return shelf_list					

def file_to_label_list(filename):
    img = Image.open(filename)
    data = tess.image_to_string(filename, lang = 'eng',config='--psm 1')
    all_lines = data.splitlines()
    list_of_little_lists = list(group_lines_into_books(all_lines, ''))
    result = remove_empty_strings(list_of_little_lists)
    result_without_punct = remove_punctuation(result)
    label_list = make_label_list(result_without_punct)
    return label_list


result = file_to_label_list(file)
print(result)


# Sort implementation after getting list of all Label objects
arrayOfLabels = result
arrayOfLabelsCopy = [0] * len(arrayOfLabels)
arrayOfIndex = [0] * len(arrayOfLabels)
for i in range(len(arrayOfLabels)):
    arrayOfLabelsCopy[i] = arrayOfLabels[i]
    arrayOfIndex[i] = i
mergeSort(arrayOfLabels)
print("For these " + str(len(arrayOfLabels)) + " books with labels in the image,")
print("From the left,")
for i in range(len(arrayOfLabels)):
    for j in range(len(arrayOfIndex)):
        if arrayOfLabelsCopy[i] == arrayOfLabels[arrayOfIndex[j]]:
            print("Book " + str((i + 1)) + " should be in position " + str((arrayOfIndex[j] + 1)))
            del arrayOfIndex[j]
            break



