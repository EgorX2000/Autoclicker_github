import webbrowser
from ahk import AHK
import keyboard
import pyautogui
import os
from datetime import datetime, timedelta
import cv2
import numpy as np

ahk = AHK()
start = datetime.now()
timeout = start + timedelta(seconds = 30)

login_path = "Buttons/login.png"
captcha_path = "Buttons/captcha.png"
get_sms_code_path = "Buttons/get_sms_code.png"


webbrowser.open_new("https://accounts.binance.com/ru/login")
pyautogui.sleep(3)

login = pyautogui.locateCenterOnScreen(login_path, confidence = 0.9)
ahk.click(login)
pyautogui.sleep(2)

captcha_x, captcha_y = pyautogui.locateCenterOnScreen(captcha_path, confidence = 0.9)
ahk.mouse_move(captcha_x, captcha_y)
#solve captcha
pyautogui.sleep(1)

get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = 0.9)
while get_sms_code == None:
    pyautogui.sleep(1)
    get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = 0.9)
ahk.click(get_sms_code)

webbrowser.open_new("https://messages.google.com/web/conversations/54")
pyautogui.sleep(3)

sms_code = None