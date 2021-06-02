import csv
import cv2
from pytesseract import pytesseract as pt
from PIL import Image
pt.tesseract_cmd = "C:\\program files\\Tesseract-OCR\\tesseract.exe"

print(pt.image_to_boxes(Image.open('33456.png')))

pt.run_tesseract('33456.png', 'output', lang=None, boxes=True, config="hocr")

# To read the coordinates
boxes = []
with open('output.box', 'rb') as f:
    reader = csv.reader(f, delimiter = ' ')
    for row in reader:
        if(len(row)==6):
            boxes.append(row)

# Draw the bounding box
img = cv2.imread('bw.png')
h, w, _ = img.shape
for b in boxes:
    img = cv2.rectangle(img,(int(b[1]),h-int(b[2])),(int(b[3]),h-int(b[4])),(255,0,0),2)

cv2.imshow('output',img)


