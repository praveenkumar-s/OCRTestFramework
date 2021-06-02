
from pytesseract import pytesseract as pt
from PIL import Image

def get_boxes(image_path):
    return pt.image_to_boxes(Image.open(image_path), output_type=pt.Output.DICT)

def get_coordinates(boxes , object_name , instance):
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
            raise "Object Not Detected"
        start=(boxes["left"][indx],boxes["bottom"][indx])
        end = (boxes["right"][indx+object_name.__len__()-1], boxes["top"][indx+object_name.__len__()-1] )

    return start,end 

def get_center_coor(image, start , end ):
    image = Image.open(image)
    width, height = image.size
    s1=(start[0],height-start[1])
    e1=(end[0],height-end[1])

    xDelta=e1[0]-s1[0]    
    yDelta=s1[1]-e1[1]
    xMid=int(xDelta/2)
    yMid=int(yDelta/2)

    return s1[0]+xMid , s1[1]-yMid


                
bx=get_boxes('33456.png')
X,Y = get_coordinates(bx, 'runtimecontguration', 2)
o = get_center_coor('33456.png',X,Y)
print(o)