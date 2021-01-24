from PIL import ImageGrab,ImageOps
import pyautogui as robot
from numpy import *


while(True):
    
    x1,y1,a,b = 731,240,65,25
    sensorSalto = (x1,y1,x1+a,y1+b)
    image = ImageGrab.grab(sensorSalto)
    fondo = ImageOps.grayscale(image)
    salto = array(fondo.getcolors())
    valorSalto = salto.sum()
    if(valorSalto != 1658):
        robot.press("space")
        
    x2,y2,a2,b2 = 730,212,44,17
    sensorAgacharse = (x2,y2,x2+a2,y2+b2)
    image = ImageGrab.grab(sensorAgacharse)
    fondo = ImageOps.grayscale(image)
    agacharse = array(fondo.getcolors())
    valueAgacharse = agacharse.sum()
    if(valueAgacharse != 715):
        robot.press('down')
 