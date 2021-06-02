from PIL import ImageGrab
import win32gui


"""
Window Name

persists the image and screen co-odrinates for the given process
"""
class AUT():
    def __init__(self, windowName) -> None:
        toplist, winlist = [], []
        def enum_cb(hwnd, results):
            winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        win32gui.EnumWindows(enum_cb, toplist)

        firefox = [(hwnd, title) for hwnd, title in winlist if windowName in title.lower()]
        # just grab the hwnd for first window matching windowname
        firefox = firefox[0]
        hwnd = firefox[0]
        win32gui.SetForegroundWindow(hwnd)
        bbox = win32gui.GetWindowRect(hwnd) # TODO Bounding Rectangle can be found here ! 
        img = ImageGrab.grab(bbox)
        img.show()

    def _getBoundingRectangleofProcess(self):
        pass
