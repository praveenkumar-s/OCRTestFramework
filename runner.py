import json
from collections import namedtuple
import imageProcessing
import pyautogui

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


def closeApplication():
    pass

for items in instructionSet:
    if(items.actionName == 'double_click'):
        double_click(items.applicationName , items.elementName , items.instance)
    elif(items.actionName == 'click' ):
        click(items.applicationName , items.elementName , items.instance)

    time.sleep(config.stepInterval)