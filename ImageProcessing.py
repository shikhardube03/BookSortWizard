from curses.ascii import isalnum
from os import remove
from cv2 import setUseOpenVX
import pytesseract as tess
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from IPython.display import display
from pytesseract import image_to_string
from PIL import Image
from sympy import sequence
import sorting

list_of_labels = []

images = ["TestImages/Label3.png", "TestImages/Label4.png", "TestImages/Label5.png", "TestImages/Label6.png", "TestImages/Label9.png", "TestImages/Label1.png", "TestImages/Label8.png", "TestImages/Label7.png"]

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

def remove_punctuation(sequence):
	# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~-'''
	for i in range(len(sequence)):
		# if sequence[i][3] contains punctuation, remove punctuation
		if sequence[i][2][0] == '-' or sequence[i][2][0] == '.':
			sequence[i][2] = sequence[i][2][1:]
	return sequence	

def make_label_list(big_list):
	l1 = sorting.Label(big_list[0][0], big_list[0][1], big_list[0][2], big_list[0][3], None)
	list_of_labels.append(l1)			


# tesseract --help-extra or tesseract --help-psm to find info about the segmentation modes
for image_file in images:
	# file = image_file
	# img = Image.open(file)

	# grayscale image
	# img = img.convert('L') 

	# OpenCV and Matplot rendering of file
	white = cv2.imread(image_file)
	gray = cv2.cvtColor(white, cv2.COLOR_BGR2GRAY)
	# ret, thresh1 = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
	cv2.imshow("thresh", gray)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# gets OCR data as string from passed image
	data = tess.image_to_string(gray, lang = 'eng',config='--psm 6')

	all_lines = data.splitlines()
	for line in all_lines:
		if line == '':
			all_lines.remove(line)

	# print('\n')

	def group_lines_into_books(sequence, separator):
		book = []
		for elem in sequence:
			if elem == separator:
				yield book
				book = []
			book.append(elem)
		yield book

	result = list(group_lines_into_books(all_lines, ''))
	result = remove_empty_strings(result)
	result = remove_punctuation(result)

	make_label_list(result)

arrayOfLabelsCopy = [0] * len(list_of_labels)
arrayOfIndex = [0] * len(list_of_labels)
for i in range(len(list_of_labels)):
    arrayOfLabelsCopy[i] = list_of_labels[i]
    arrayOfIndex[i] = i
mergeSort(list_of_labels)
print("For these " + str(len(list_of_labels)) + " books with labels in the image,")
print("From the left,")
for i in range(len(list_of_labels)):
    for j in range(len(arrayOfIndex)):
        if arrayOfLabelsCopy[i] == list_of_labels[arrayOfIndex[j]]:
            print("Book " + str((i + 1)) + " should be in position " + str((arrayOfIndex[j] + 1)))
            del arrayOfIndex[j]
            break



