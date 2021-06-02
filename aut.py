

from PIL import ImageGrab
import win32gui


"""
Window Name
persists the image and screen co-odrinates for the given process
"""
toplist, winlist = [], []


def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


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
        self.imagePath= 'aut_img_'+str(hwnd)+'.png'

    def _getBoundingRectangleofProcess(self):
        pass


