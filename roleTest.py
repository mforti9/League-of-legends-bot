import pyautogui
import smtplib
from datetime import datetime
import time
import schedule
import requests



def role():
    #adcarry = pyautogui.locateCenterOnScreen('images/adcarry.png', confidence=0.7)
    jungle = pyautogui.locateCenterOnScreen('jungle.png', confidence=0.7)
    #mid = pyautogui.locateCenterOnScreen('mid.png', confidence=0.7)
    #supp = pyautogui.locateCenterOnScreen('supp.png', confidence=0.7)
    #top = pyautogui.locateCenterOnScreen('top.png', confidence=0.7)
    while True:
        if jungle:
            print ("jungle")
        # elif adcarry:
        #     return "AD"
        # elif mid:
        #     return "Mid"
        # elif supp:
        #     return "Supp"
        # elif top:
        #     return "Top"
        else:
            time.sleep(3)
            print (datetime.now())
        

role()