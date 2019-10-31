import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2
import os
import pytesseract
import pyautogui as g

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

qafile = open("Ques.txt","r")
qafile = qafile.read()
qafile = qafile.strip()
qafile.replace("\n","")
qafile = qafile.split(",")



font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    printscreen_pil =  ImageGrab.grab(bbox=(432,240, 1050 ,500))
    printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 
    printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2GRAY)
    #ret,printscreen_numpy = cv2.threshold(printscreen_numpy,127,255,cv2.THRESH_BINARY)
    filename = "images/{}.jpg".format(os.getpid())
    cv2.imwrite(filename,printscreen_numpy)
    text = pytesseract.image_to_string(Image.open(filename))
    text = text.replace(" ","")
    print(text)
    print(qafile)
    cv2.putText(printscreen_numpy,str("".join(qafile)),(100,100), font, 1,(0,0,0),2,cv2.LINE_AA)
    text = text.replace("—","-")
    text = text.replace("""oe

0.71""","0.71")
    text = text.replace("0.7171","0.71")
    cv2.putText(printscreen_numpy,str(text),(30,200), font, 1,(0,0,0),2,cv2.LINE_AA)
    try:
        print(qafile[qafile.index(text) + 1])
        cv2.putText(printscreen_numpy,qafile[qafile.index(text) + 1],(10,100), font, 1,(0,0,0),2,cv2.LINE_AA)

        g.click(x=604, y=395) # click text box
        g.typewrite(qafile[qafile.index(text) + 1])   #type something..
        #f = input()
        #printscreen_numpy = cv2.putText(printscreen_numpy,qafile[qafile.index(text) + 1],(10,100), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    except ValueError:
        print("'{}' Not Found.".format(text))
    cv2.imshow('Screen Capture {}'.format(os.getpid()),printscreen_numpy)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
    #print(text)