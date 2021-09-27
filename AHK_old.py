import webbrowser
from ahk import AHK
import keyboard
import pyautogui
import os
from datetime import datetime, timedelta
import cv2
import numpy as np

ahk = AHK()

login_path = "Buttons/login.png"
captcha_path = "Buttons/captcha.png"
get_sms_code_path = "Buttons/get_sms_code.png"
sms_code_form_path = "Buttons/sms_code_form.png"
main_page_url_path = "Buttons/main_page_url.png"


webbrowser.open_new("https://accounts.binance.com/ru/login")

login = pyautogui.locateCenterOnScreen(login_path, confidence = 0.9)
while login == None:
    pyautogui.sleep(0.1)
    login = pyautogui.locateCenterOnScreen(login_path, confidence = 0.9)
ahk.click(login)

captcha = pyautogui.locateCenterOnScreen(captcha_path, confidence = 0.9)
while captcha == None:
    pyautogui.sleep(0.1)
    captcha = pyautogui.locateCenterOnScreen(captcha_path, confidence = 0.9)
ahk.click(captcha)
#solve captcha

get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = 0.9)
while get_sms_code == None:
    pyautogui.sleep(0.1)
    get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = 0.9)
ahk.click(get_sms_code)

webbrowser.open_new("https://messages.google.com/web/conversations/54")
#parse sms
pyautogui.sleep(10)

keyboard.press_and_release("Ctrl+w")

sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = 0.9)
while sms_code_form == None:
    pyautogui.sleep(0.1)
    sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = 0.9)
ahk.click(sms_code_form)

keyboard.press_and_release("Ctrl+v")

main_page_url = pyautogui.locateCenterOnScreen(main_page_url_path, confidence = 0.9)
while main_page_url == None:
    pyautogui.sleep(0.1)
    main_page_url = pyautogui.locateCenterOnScreen(main_page_url_path, confidence = 0.9)
ahk.click(main_page_url)
ahk.type("https://www.binance.com/ru/trade/BTC_USDT?layout=basic")

keyboard.press_and_release("Enter")