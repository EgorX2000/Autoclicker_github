import webbrowser
from ahk import AHK
import keyboard
import pyautogui
import os
from datetime import datetime, timedelta
import cv2
import numpy as np
import pytesseract
import math

ahk = AHK()
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

start = datetime.now()
timeout = start + timedelta(seconds = 10)

settings_path = "Buttons/settings.png"
scale_check_path = "Buttons/scale_check.png"
main_page_url_path = "Buttons/main_page_url.png"

dark_theme_path = cv2.imread("Buttons/dark_theme_175.png", cv2.IMREAD_UNCHANGED)
light_theme_path = cv2.imread("Buttons/light_theme_175.png", cv2.IMREAD_UNCHANGED)
email_path = cv2.imread("Buttons/email_175.png", cv2.IMREAD_UNCHANGED)
password_path = cv2.imread("Buttons/password_175.png", cv2.IMREAD_UNCHANGED)
login_path = cv2.imread("Buttons/login_175.png", cv2.IMREAD_UNCHANGED)
captcha_path = cv2.imread("Buttons/captcha_175.png", cv2.IMREAD_UNCHANGED)
get_sms_code_path = cv2.imread("Buttons/get_sms_code_175.png", cv2.IMREAD_UNCHANGED)
sms_check_path = cv2.imread("Buttons/sms_check_175.png", cv2.IMREAD_UNCHANGED)
sms_path = cv2.imread("Buttons/sms_175.png", cv2.IMREAD_UNCHANGED)
sms_code_form_path = cv2.imread("Buttons/sms_code_form_175.png", cv2.IMREAD_UNCHANGED)

webbrowser.open_new("https://accounts.binance.com/ru/login")

settings = pyautogui.locateCenterOnScreen(settings_path, confidence = 0.9)
while settings == None:
    pyautogui.sleep(0.1)
    settings = pyautogui.locateCenterOnScreen(settings_path, confidence = 0.9)
ahk.click(settings)

scale_check = pyautogui.locateOnScreen(scale_check_path, confidence = 0.8)
while scale_check == None:
    pyautogui.sleep(0.1)
    scale_check = pyautogui.locateOnScreen(scale_check_path, confidence = 0.8)
scale_check = pyautogui.screenshot(region=(scale_check))
scale_text = pytesseract.image_to_string(scale_check)
scale = scale_text.replace("%", "")
scale = int(scale)
scale = scale / 175
keyboard.press_and_release("Esc")

#if dark_theme == None and light_theme == None:
#    for i in range(scale - 25, scale + 25 + 1):
#        
#
#        dark_theme_path_width = int(dark_theme_path.shape[1] * i / 100)#
#        dark_theme_path_height = int(dark_theme_path.shape[0] * i / 100)
#        dark_theme_path_dsize = (dark_theme_path_width, dark_theme_path_height)
#        light_theme_path_width = int(light_theme_path.shape[1] * i / 100)#
#        light_theme_path_height = int(light_theme_path.shape[0] * i / 100)
#        light_theme_path_dsize = (light_theme_path_width, light_theme_path_height)
#
#        dark_theme_path = cv2.resize(dark_theme_path, dark_theme_path_dsize, interpolation = cv2.INTER_AREA)
#        light_theme_path = cv2.resize(light_theme_path, light_theme_path_dsize, interpolation = cv2.INTER_AREA)
#
#        cv2.imwrite("Buttons/dark_theme_scaled.png", dark_theme_path)
#        cv2.imwrite("Buttons/light_theme_scaled.png", light_theme_path)
#
#        dark_theme_path = "Buttons/dark_theme_scaled.png"
#        light_theme_path = "Buttons/light_theme_scaled.png"
#
#        dark_theme = pyautogui.locateCenterOnScreen(dark_theme_path, confidence = 0.9)
#        light_theme = pyautogui.locateCenterOnScreen(light_theme_path, confidence = 0.9)
#
#        if dark_theme:
#            scale = i / 100
#            ahk.click(dark_theme)
#            break
#        
#        elif light_theme:
#            scale = i / 100
#            break


dark_theme_path_width = int(dark_theme_path.shape[1] * scale)#
dark_theme_path_height = int(dark_theme_path.shape[0] * scale)
dark_theme_path_dsize = (dark_theme_path_width, dark_theme_path_height)
light_theme_path_width = int(light_theme_path.shape[1] * scale)#
light_theme_path_height = int(light_theme_path.shape[0] * scale)
light_theme_path_dsize = (light_theme_path_width, light_theme_path_height)
email_path_width = int(email_path.shape[1] * scale)#
email_path_height = int(email_path.shape[0] * scale)
email_path_dsize = (email_path_width, email_path_height)
password_path_width = int(password_path.shape[1] * scale)#
password_path_height = int(password_path.shape[0] * scale)
password_path_dsize = (password_path_width, password_path_height)
login_path_width = int(login_path.shape[1] * scale)#
login_path_height = int(login_path.shape[0] * scale)
login_path_dsize = (login_path_width, login_path_height)
captcha_path_width = int(captcha_path.shape[1] * scale)#
captcha_path_height = int(captcha_path.shape[0] * scale)
captcha_path_dsize = (captcha_path_width, captcha_path_height)
get_sms_code_path_width = int(get_sms_code_path.shape[1] * scale)#
get_sms_code_path_height = int(get_sms_code_path.shape[0] * scale)
get_sms_code_path_dsize = (get_sms_code_path_width, get_sms_code_path_height)
sms_check_path_width = int(sms_check_path.shape[1] * scale)#
sms_check_path_height = int(sms_check_path.shape[0] * scale)
sms_check_path_dsize = (sms_check_path_width, sms_check_path_height)
sms_path_width = int(sms_path.shape[1] * scale)#
sms_path_height = int(sms_path.shape[0] * scale)
sms_path_dsize = (sms_path_width, sms_path_height)
sms_code_form_path_width = int(sms_code_form_path.shape[1] * scale)#
sms_code_form_path_height = int(sms_code_form_path.shape[0] * scale)
sms_code_form_path_dsize = (sms_code_form_path_width, sms_code_form_path_height)

dark_theme_path = cv2.resize(dark_theme_path, dark_theme_path_dsize, interpolation = cv2.INTER_AREA)
light_theme_path = cv2.resize(light_theme_path, light_theme_path_dsize, interpolation = cv2.INTER_AREA)
email_path = cv2.resize(email_path, email_path_dsize, interpolation = cv2.INTER_AREA)
password_path = cv2.resize(password_path, password_path_dsize, interpolation = cv2.INTER_AREA)
login_path = cv2.resize(login_path, login_path_dsize, interpolation = cv2.INTER_AREA)
captcha_path = cv2.resize(captcha_path, captcha_path_dsize, interpolation = cv2.INTER_AREA)
get_sms_code_path = cv2.resize(get_sms_code_path, get_sms_code_path_dsize, interpolation = cv2.INTER_AREA)
sms_check_path = cv2.resize(sms_check_path, sms_check_path_dsize, interpolation = cv2.INTER_AREA)
sms_path = cv2.resize(sms_path, sms_path_dsize, interpolation = cv2.INTER_AREA)
sms_code_form_path = cv2.resize(sms_code_form_path, sms_code_form_path_dsize, interpolation = cv2.INTER_AREA)

cv2.imwrite("Buttons/dark_theme_scaled.png", dark_theme_path)
cv2.imwrite("Buttons/light_theme_scaled.png", light_theme_path)
cv2.imwrite("Buttons/email_scaled.png", email_path)
cv2.imwrite("Buttons/password_scaled.png", password_path)
cv2.imwrite("Buttons/login_scaled.png", login_path)
cv2.imwrite("Buttons/captcha_scaled.png", captcha_path)
cv2.imwrite("Buttons/get_sms_code_scaled.png", get_sms_code_path)
cv2.imwrite("Buttons/sms_check_scaled.png", sms_check_path)
cv2.imwrite("Buttons/sms_scaled.png", sms_path)
cv2.imwrite("Buttons/sms_code_form_scaled.png", sms_code_form_path)

dark_theme_path = "Buttons/dark_theme_scaled.png"
light_theme_path = "Buttons/light_theme_scaled.png"
email_path = "Buttons/email_scaled.png"
password_path = "Buttons/password_scaled.png"
login_path = "Buttons/login_scaled.png"
captcha_path = "Buttons/captcha_scaled.png"
get_sms_code_path = "Buttons/get_sms_code_scaled.png"
sms_check_path = "Buttons/sms_check_scaled.png"
sms_path = "Buttons/sms_scaled.png"
sms_code_form_path = "Buttons/sms_code_form_scaled.png"

dark_theme = pyautogui.locateCenterOnScreen(dark_theme_path, confidence = 0.8)
light_theme = pyautogui.locateCenterOnScreen(light_theme_path, confidence = 0.8)
while dark_theme == None and light_theme == None:
    pyautogui.sleep(0.1)
    dark_theme = pyautogui.locateCenterOnScreen(dark_theme_path, confidence = 0.8)
    light_theme = pyautogui.locateCenterOnScreen(light_theme_path, confidence = 0.8)
ahk.click(dark_theme)

email = pyautogui.locateCenterOnScreen(email_path, confidence = 0.9)
while email == None:
    pyautogui.sleep(0.1)
    email = pyautogui.locateCenterOnScreen(email_path, confidence = 0.9)
ahk.click(email)
ahk.type("ebkrivoshapkin@gmail.com")

password = pyautogui.locateCenterOnScreen(password_path, confidence = 0.9)
while password == None:
    pyautogui.sleep(0.1)
    password = pyautogui.locateCenterOnScreen(password_path, confidence = 0.9)
ahk.click(password)
ahk.type("")

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
sms_check = pyautogui.locateCenterOnScreen(sms_check_path, confidence = 0.8)
while sms_check == None:
    pyautogui.sleep(0.1)
    sms_check = pyautogui.locateCenterOnScreen(sms_check_path, confidence = 0.8)
if sms_check:
    sms = pyautogui.locateOnScreen(sms_path, confidence = 0.9)
    while sms == None:
        pyautogui.sleep(0.1)
        sms = pyautogui.locateOnScreen(sms_path, confidence = 0.9)
    sms = pyautogui.screenshot(region=(sms))
sms_text = pytesseract.image_to_string(sms)
sms_code = str(sms_text.split()[3])
sms_code = sms_code.replace(".", "")
sms_code = sms_code.strip()

keyboard.press_and_release("Ctrl+w")

sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = 0.9)
while sms_code_form == None:
    pyautogui.sleep(0.1)
    sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = 0.9)
ahk.click(sms_code_form)

ahk.type(sms_code)

main_page_url = pyautogui.locateCenterOnScreen(main_page_url_path, confidence = 0.9)
while main_page_url == None:
    pyautogui.sleep(0.1)
    main_page_url = pyautogui.locateCenterOnScreen(main_page_url_path, confidence = 0.9)
ahk.click(main_page_url)
ahk.type("https://www.binance.com/ru/trade/BTC_USDT?layout=basic")
keyboard.press_and_release("Enter")
