import aut
import imageProcessing



application = 'Cougar Diagnostics'

IP = imageProcessing.ImageProcessing(windowName=application)
co= IP.findElement('Machine Layers')
print(co)
