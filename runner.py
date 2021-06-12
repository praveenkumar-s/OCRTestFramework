import json
from collections import namedtuple
import imageProcessing
import pyautogui
import time

def customJsonDecoder(dictVar):
    return namedtuple('X', dictVar.keys())(*dictVar.values())

input_file = json.load(open('instructionSet.json'), object_hook=customJsonDecoder)

instructionSet= input_file.instructions

config = input_file.config

def double_click(application, element, instance ):
    IP = imageProcessing.ImageProcessing(windowName=application)
    coOrdinates = IP.findElement(element , instance=instance)
    pyautogui.doubleClick(coOrdinates[0],coOrdinates[1])

def click(application, element, instance ):
    IP = imageProcessing.ImageProcessing(windowName=application)
    coOrdinates = IP.findElement(element , instance=instance)
    pyautogui.click(coOrdinates[0],coOrdinates[1])

def close_application(application):
    IP = imageProcessing.ImageProcessing(windowName=application)
    coOrdinates = IP.closeApplication()
    pyautogui.click(coOrdinates[0], coOrdinates[1])
    pyautogui.click(coOrdinates[0], coOrdinates[1])

def closeApplication():
    pass

for items in instructionSet:
    if(items.enabled):
        continue
    print("Running item : "+ str(items))
    isRegx = "Regx" in items.args
    IP = imageProcessing.ImageProcessing(windowName=items.applicationName)
    coOrdinates = IP.findElement(items.elementName , items.instance , isRegex=isRegx)

    if(items.actionName == 'double_click'):
        pyautogui.doubleClick(coOrdinates[0],coOrdinates[1])
    elif(items.actionName == 'click' ):
        pyautogui.click(coOrdinates[0],coOrdinates[1])
    elif(items.actionName == 'close_application'):
        pyautogui.click(coOrdinates[0], coOrdinates[1])
        time.sleep(0.3)
        pyautogui.click(coOrdinates[0], coOrdinates[1])

    time.sleep(input_file.config.stepInterval)