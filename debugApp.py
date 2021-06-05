import aut
import imageProcessing
import pyautogui


application = 'Cougar Diagnostics'

IP = imageProcessing.ImageProcessing(windowName=application)
co = IP.findElement('MachineLayers')
print(str(co))

pyautogui.click(co[0], co[1])

pyautogui.doubleClick(co[0], co[1])

IP = imageProcessing.ImageProcessing(windowName=application)
co = IP.findElement('Channels')


pyautogui.doubleClick(co[0], co[1])
