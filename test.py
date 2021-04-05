import pyautogui
import smtplib
from datetime import datetime
import time
import schedule
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1772044424:AAGqBf4NHewqVh7euT4xMa9501Q38M5oCZ0'
    bot_chatID = '1155667601'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

""" def champ_select():
    while True:
        champSelect = pyautogui.locateCenterOnScreen('champSelect.png', confidence=0.7)
        if champSelect:
            telegram_bot_sendtext(f'In Champ Select! {datetime.now()}') 
            print("match_found")
            break
        else:
            pass
            time.sleep(3)
            print(datetime.now())
 """
def jobTest():
    while True:
        # locate trigger on screen
        accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
        loading = pyautogui.locateCenterOnScreen('loading.png', confidence=0.7)
        champSelect = pyautogui.locateCenterOnScreen('champSelect.png', confidence=0.7)
        if accept:
            pyautogui.moveTo(accept)
            # click multiple times to ensure clicked
            pyautogui.click(accept)
            pyautogui.click(accept)
            pyautogui.click(accept)
            pyautogui.click()

            print(f'Game Accepted. {datetime.now()}')

            telegram_bot_sendtext(f'Game is ready! {datetime.now()}')

            #champ_select()

            time.sleep(5)

            
        elif champSelect:
            telegram_bot_sendtext(f'In Champ Select! {datetime.now()}') 
            
        # elif loading:
        #     telegram_bot_sendtext(f'Game Loading! {datetime.now()}')
        #     return schedule.CancelJob

        else:
            pass
            print(datetime.now())
    
schedule.every(3).seconds.do(jobTest())
# champ_select()