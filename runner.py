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
    if(not items.enabled):
        continue
    print("Running item : "+ str(items))
    isRegx = "Regx" in items.args
    IP = imageProcessing.ImageProcessing(windowName=items.applicationName)

    if(items.actionName == 'double_click'):
        coOrdinates = IP.findElement(items.elementName , items.instance , isRegex=isRegx)
        pyautogui.doubleClick(coOrdinates[0],coOrdinates[1])
    elif(items.actionName == 'click' ):
        coOrdinates = IP.findElement(items.elementName , items.instance , isRegex=isRegx)
        pyautogui.click(coOrdinates[0],coOrdinates[1])
    elif(items.actionName == 'close_application'):
        coOrdinates = IP.findElement(items.elementName , items.instance , isRegex=isRegx)
        pyautogui.click(coOrdinates[0], coOrdinates[1])
        time.sleep(0.3)
        pyautogui.click(coOrdinates[0], coOrdinates[1])
    elif(items.actionName == 'assertExits'):
        coOrdinates = IP.findElement(items.elementName , items.instance , isRegex=isRegx)
    elif(items.actionName == 'assertNotExits'):
        found = False
        try:
            coOrdinates = IP.findElement(items.elementName , items.instance , isRegex=isRegx)    
            found = True
        except:
            pass
        if(found):
            raise Exception("Assertion Failed. Control unexpected , but exists")
            


    time.sleep(input_file.config.stepInterval)