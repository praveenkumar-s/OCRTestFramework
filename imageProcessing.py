
from pytesseract import pytesseract as pt
from PIL import Image


"""
Init -> (optional) Image 
findElement -> Returns the co-ordinates of the given text and instances
findElements -> Returns list of occurences of a given string
"""
class ImageProcessing():
    def __init__(self,imagePath=None) -> None:
        pass
    
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
