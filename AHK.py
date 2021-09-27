import webbrowser
from ahk import AHK
import keyboard
import pyautogui
import os
from datetime import datetime, timedelta
import cv2
import numpy as np
import pytesseract

ahk = AHK()
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

start = datetime.now()
timeout = start + timedelta(seconds = 10)

dark_theme_path = "Buttons/dark_theme.png"
light_theme_path = "Buttons/light_theme.png"
login_path = "Buttons/login.png"
captcha_path = "Buttons/captcha.png"
get_sms_code_path = "Buttons/get_sms_code.png"
sms_check_path = "Buttons/sms_check.png"
sms_path = "Buttons/sms.png"
sms_code_form_path = "Buttons/sms_code_form.png"
main_page_url_path = "Buttons/main_page_url.png"


webbrowser.open_new("https://accounts.binance.com/ru/login")

dark_theme = pyautogui.locateCenterOnScreen(dark_theme_path, confidence = 0.95)
light_theme = pyautogui.locateCenterOnScreen(light_theme_path, confidence = 0.95)
while dark_theme == None and light_theme == None:
    pyautogui.sleep(0.1)
    dark_theme = pyautogui.locateCenterOnScreen(dark_theme_path, confidence = 0.95)
    light_theme = pyautogui.locateCenterOnScreen(light_theme_path, confidence = 0.95)
    start = datetime.now()
ahk.click(dark_theme)

login = pyautogui.locateCenterOnScreen(login_path, confidence = 0.95)
while login == None:
    pyautogui.sleep(0.1)
    login = pyautogui.locateCenterOnScreen(login_path, confidence = 0.95)
ahk.click(login)

captcha = pyautogui.locateCenterOnScreen(captcha_path, confidence = 0.95)
while captcha == None:
    pyautogui.sleep(0.1)
    captcha = pyautogui.locateCenterOnScreen(captcha_path, confidence = 0.95)
ahk.click(captcha)
#solve captcha

get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = 0.95)
while get_sms_code == None:
    pyautogui.sleep(0.1)
    get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = 0.95)
ahk.click(get_sms_code)

webbrowser.open_new("https://messages.google.com/web/conversations/54")
#parse sms
sms_check = pyautogui.locateCenterOnScreen(sms_check_path, confidence = 0.95)
while sms_check == None:
    pyautogui.sleep(0.1)
    sms_check = pyautogui.locateCenterOnScreen(sms_check_path, confidence = 0.95)
if sms_check:
    sms = pyautogui.locateOnScreen(sms_path, confidence = 0.9)
    while sms == None:
        pyautogui.sleep(0.1)
        sms = pyautogui.locateOnScreen(sms_path, confidence = 0.9)
    sms = pyautogui.screenshot(region=(sms))
sms_code = str()
count = 0
sms_text = pytesseract.image_to_string(sms)
sms_code = str(sms_text.split()[3])
sms_code = sms_code.replace(".", "")
sms_code = sms_code.strip()

keyboard.press_and_release("Ctrl+w")

sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = 0.95)
while sms_code_form == None:
    pyautogui.sleep(0.1)
    sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = 0.95)
ahk.click(sms_code_form)

ahk.type(sms_code)

main_page_url = pyautogui.locateCenterOnScreen(main_page_url_path, confidence = 0.95)
while main_page_url == None:
    pyautogui.sleep(0.1)
    main_page_url = pyautogui.locateCenterOnScreen(main_page_url_path, confidence = 0.95)
ahk.click(main_page_url)
ahk.type("https://www.binance.com/ru/trade/BTC_USDT?layout=basic")
keyboard.press_and_release("Enter")