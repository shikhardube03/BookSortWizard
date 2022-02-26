import pytesseract as tess
from pytesseract import image_to_string
from PIL import Image
import cv2

# tesseract --help-extra or tesseract --help-psm to find info about the segmentation modes

img = Image.open("Label1.png")
img = img.convert('L') # convert image to black and white

data = tess.image_to_string(img, lang = 'eng',config='--psm 1')

# all_lines = data.splitlines()
print(data)

all_lines = data.splitlines()

def group_lines_into_books(sequence, separator):
    book = []
    for elem in sequence:
        if elem == separator:
            yield book
            book = []
        book.append(elem)
    yield book

result = list(group_lines_into_books(all_lines, ''))
print(result)

