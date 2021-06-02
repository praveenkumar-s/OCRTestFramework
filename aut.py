
import cv2
import os
from PIL import ImageGrab,Image
import win32gui


"""
Window Name
persists the image and screen co-odrinates for the given process
"""
toplist, winlist = [], []


def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


def preprocessImage(imgLoc, saveAs):
    image = cv2.imread(imgLoc)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold( gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = "{}.png".format(saveAs)
	cv2.imwrite(filename, gray)

class AUT():
    def __init__(self, windowName) -> None:
        self.windowName = windowName
        win32gui.EnumWindows(enum_cb, toplist)
        for items in winlist:
            if(items[1] == windowName):
                firefox = items
                break
            else:
                firefox = []
        print(firefox)
        firefox = firefox[0]
        hwnd = firefox
        win32gui.SetForegroundWindow(hwnd)
        # TODO Bounding Rectangle can be found here !
        bbox = win32gui.GetWindowRect(hwnd)
        self.boundingRectangle = bbox
        img = ImageGrab.grab(bbox)
        img.save('aut_img_'+str(hwnd)+'.png')
        preprocessImage('aut_img_'+str(hwnd)+'.png', 'aut_img_'+str(hwnd)+'PROCESSED.png')
        self.imagePath= 'aut_img_'+str(hwnd)+'PROCESSED.png'

    def _getBoundingRectangleofProcess(self):
        pass


