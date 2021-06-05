
import re
from pytesseract import pytesseract as pt
from PIL import Image
import aut
import logging
logging.basicConfig(filename='ImageProcessing.log', 
level=logging.DEBUG, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

pt.tesseract_cmd = "C:\\program files\\Tesseract-OCR\\tesseract.exe"
"""
Init -> (optional) Image 
findElement -> Returns the co-ordinates of the given text and instances
findElements -> Returns list of occurences of a given string
"""
class ImageProcessing():
    def __init__(self,windowName=None,imagePath=None,isDebug=True) -> None:
        self.appUnderTest=None
        self.isDebug = isDebug
        if(windowName is not None):
            self.appUnderTest = aut.AUT(windowName)
            self.imagePath = self.appUnderTest.imagePath
        elif(imagePath is not None):
            self.imagePath = imagePath
        else:
            raise Exception("Either AUT or imagePath is mandatory ")
    def _debugInformation(self):
        if(self.isDebug):
            detectionData = pt.image_to_string(Image.open(self.imagePath))
            logging.debug(detectionData)

    def _getBoxes(self):
        return pt.image_to_boxes(Image.open(self.imagePath), output_type=pt.Output.DICT)
    
    def _getCoOrdinates(self, boxes , object_name , instance):
        overall_string= ''.join(boxes['char'])
        overall_string.replace(' ','')
        current_indx=0
        
        while instance>1:
            indx = str.find(overall_string , object_name, current_indx)
            if(indx==-1):
                raise "Object Not Detected"
            else:
                instance=instance-1
                current_indx=indx+1

        if(instance==1):
            indx = str.find(overall_string,object_name, current_indx)
            if(indx==-1):
                raise Exception("Object Not Detected")
            start=(boxes["left"][indx],boxes["bottom"][indx])
            end = (boxes["right"][indx+object_name.__len__()-1], boxes["top"][indx+object_name.__len__()-1] )

        return start,end 
    
    def _getCenterCoOrdinates(self,start,end):
            image = Image.open(self.imagePath)
            width, height = image.size
            s1=(start[0],height-start[1])
            e1=(end[0],height-end[1])

            xDelta=e1[0]-s1[0]    
            yDelta=s1[1]-e1[1]
            xMid=int(xDelta/2)
            yMid=int(yDelta/2)
            return s1[0]+xMid , s1[1]-yMid

    def findElement(self,name,instance,offset=None):
        if(self.appUnderTest is not None):
            self.appUnderTest = aut.AUT(self.appUnderTest.windowName)
            self.imagePath = self.appUnderTest.imagePath
        self._debugInformation()
        bx = self._getBoxes()
        X,Y=self._getCoOrdinates(bx,name,instance)
        o=self._getCenterCoOrdinates( X , Y )
        if(self.appUnderTest is not None):
            boundingRect = self.appUnderTest.boundingRectangle
            adjusted = (o[0]+boundingRect[0], o[1]+boundingRect[1])
            o=adjusted
        if(offset is not None):
            adju2 = (o[0]+offset[0], o[1],offset[1])
            o=adju2
        return o 
