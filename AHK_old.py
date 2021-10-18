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