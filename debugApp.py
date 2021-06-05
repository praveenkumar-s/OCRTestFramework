import aut
import imageProcessing
import pyautogui


application = 'Cougar Diagnostics'

IP = imageProcessing.ImageProcessing(windowName=application)
co= IP.findElement('Machine Layers')


pyautogui.click(co[0],co[1])


