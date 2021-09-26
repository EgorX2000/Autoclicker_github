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

sms_code = None