import pyautogui
import smtplib
from datetime import datetime
import time
import schedule
import requests
from telegramListener import listener 
   

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1772044424:AAGqBf4NHewqVh7euT4xMa9501Q38M5oCZ0'
    bot_chatID = '1155667601'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def champ_select():
    time.sleep(5)
    while True:
        #champSelect = pyautogui.locateCenterOnScreen('champSelect.png', confidence=0.7)
        accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
        yourTurn = pyautogui.locateCenterOnScreen('yourTurn.png', confidence=0.7)
        loading = pyautogui.locateCenterOnScreen('loading.png', confidence=0.7)
        dodged = pyautogui.locateCenterOnScreen('inQueue.png', confidence=0.7)
        # if champSelect:
        #     telegram_bot_sendtext(f'In Champ Select! {datetime.now()}') 
        #     print("Match Found")
        if yourTurn:
            role()
        elif dodged:
            telegram_bot_sendtext(f'Someone Dodged! {datetime.now()}') 
            print('someone dodged!')
            return
        elif accept:
            return
        elif loading:
            telegram_bot_sendtext(f'Game Loading! {datetime.now()}')
            quit()
        else:
            pass
            time.sleep(3) 
            print("debug: inner function")
            print(datetime.now())

def role():
    #adcarry = pyautogui.locateCenterOnScreen('images/adcarry.png', confidence=0.7)
    jungle = pyautogui.locateCenterOnScreen('images/jungle.png', confidence=0.7)
    #mid = pyautogui.locateCenterOnScreen('mid.png', confidence=0.7)
    #supp = pyautogui.locateCenterOnScreen('supp.png', confidence=0.7)
    #top = pyautogui.locateCenterOnScreen('top.png', confidence=0.7)
    accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
    while True:
        if jungle:
            print('You got Jungle!')
            listener()
            return
        # elif adcarry:
        #     return "AD"
        # elif mid:
        #     return "Mid"
        # elif supp:
        #     return "Supp"
        # elif top:
        #     return "Top"
        elif accept:
            #if someone dodges, should return back to original while loop
            return
        else:
            time.sleep(3)
            print("checking role...")
    #exec('telegramListener.py')
            

if __name__ == "__main__":
    while True:
        # locate trigger on screen
        accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
        loading = pyautogui.locateCenterOnScreen('loading.png', confidence=0.7)
        #champSelect = pyautogui.locateCenterOnScreen('champSelect.png', confidence=0.7)
        if accept:
            pyautogui.moveTo(accept)
            # click multiple times to ensure clicked
            pyautogui.click(accept)
            pyautogui.click(accept)
            pyautogui.click(accept)
            pyautogui.click()

            print(f'Game Accepted. {datetime.now()}')

            telegram_bot_sendtext(f'Game is ready! {datetime.now()}')
            #call champ_select function which handles arguments during champ select and exits if someone dodges
            champ_select()
            
        elif loading:
            telegram_bot_sendtext(f'Game Loading! {datetime.now()}')
            quit()

        else:
            pass
            time.sleep(3)
            print("debug: outer function")
            print(datetime.now())