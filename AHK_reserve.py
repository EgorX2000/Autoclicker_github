import webbrowser
from ahk import AHK
from ahk.window import Window
import keyboard
import pyautogui
import os
from datetime import datetime, timedelta
import cv2
import numpy as np
import pytesseract
import math
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ahk = AHK()
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

dark_theme_switch_path = "Buttons/dark_theme_switch_175.png"
light_theme_switch_path = "Buttons/light_theme_switch_175.png"

email_path = cv2.imread("Buttons/email_175.png", cv2.IMREAD_UNCHANGED)
password_path = cv2.imread("Buttons/password_175.png", cv2.IMREAD_UNCHANGED)
login_path = cv2.imread("Buttons/login_175.png", cv2.IMREAD_UNCHANGED)
captcha_path = cv2.imread("Buttons/captcha_175.png", cv2.IMREAD_UNCHANGED)
get_sms_code_path = cv2.imread("Buttons/get_sms_code_175.png", cv2.IMREAD_UNCHANGED)
sms_check_path = cv2.imread("Buttons/sms_check_175.png", cv2.IMREAD_UNCHANGED)
sms_path = cv2.imread("Buttons/sms_175.png", cv2.IMREAD_UNCHANGED)
sms_code_form_path = cv2.imread("Buttons/sms_code_form_175.png", cv2.IMREAD_UNCHANGED)
sms_code_form_check_path = cv2.imread("Buttons/sms_code_form_check_175.png", cv2.IMREAD_UNCHANGED)

driver = webdriver.Chrome("D:/Документы/Python/Autoclicker_test/Chromedriver/chromedriver.exe", chrome_options = options)
driver.get("https://www.binance.com/ru/trade/BTC_USDT?layout=basic")

webbrowser.open_new("https://accounts.binance.com/ru/login")

browser = ahk.active_window 

browser.maximize()

#pyautogui.sleep(3)

dark_theme_switch = pyautogui.locateCenterOnScreen(dark_theme_switch_path, confidence = 0.85)
light_theme_switch = pyautogui.locateCenterOnScreen(light_theme_switch_path, confidence = 0.9)
if dark_theme_switch == None and light_theme_switch == None:
    for i in range(20, 110 + 1, 4):
        dark_theme_switch_path = cv2.imread("Buttons/dark_theme_switch_175.png", cv2.IMREAD_UNCHANGED)
        light_theme_switch_path = cv2.imread("Buttons/light_theme_switch_175.png", cv2.IMREAD_UNCHANGED)

        dark_theme_switch_path_width = int(dark_theme_switch_path.shape[1] * i / 100)#
        dark_theme_switch_path_height = int(dark_theme_switch_path.shape[0] * i / 100)
        dark_theme_switch_path_dsize = (dark_theme_switch_path_width, dark_theme_switch_path_height)
        light_theme_switch_path_width = int(light_theme_switch_path.shape[1] * i / 100)#
        light_theme_switch_path_height = int(light_theme_switch_path.shape[0] * i / 100)
        light_theme_switch_path_dsize = (light_theme_switch_path_width, light_theme_switch_path_height)

        dark_theme_switch_path = cv2.resize(dark_theme_switch_path, dark_theme_switch_path_dsize, interpolation = cv2.INTER_AREA)
        light_theme_switch_path = cv2.resize(light_theme_switch_path, light_theme_switch_path_dsize, interpolation = cv2.INTER_AREA)

        cv2.imwrite("Buttons/dark_theme_switch_scaled.png", dark_theme_switch_path)
        cv2.imwrite("Buttons/light_theme_switch_scaled.png", light_theme_switch_path)

        dark_theme_switch_path = "Buttons/dark_theme_switch_scaled.png"
        light_theme_switch_path = "Buttons/light_theme_switch_scaled.png"

        dark_theme_switch = pyautogui.locateCenterOnScreen(dark_theme_switch_path, confidence = 0.85)
        light_theme_switch = pyautogui.locateCenterOnScreen(light_theme_switch_path, confidence = 0.9)

        if dark_theme_switch:
            scale = i / 100
            ahk.click(dark_theme_switch)
            print("1st scaling success", scale)
            print("dark_theme_switch success")
            break
        
        elif light_theme_switch:
            scale = i / 100
            print("1st scaling success", scale)
            break
        
elif dark_theme_switch:
    scale = 1
    conf = 0.85
    ahk.click(dark_theme_switch)
    print("scaling success", scale)

else:
    scale = 1
    conf = 0.85
    print("scaling success", scale)


password_path_width = int(password_path.shape[1] * scale)#
password_path_height = int(password_path.shape[0] * scale)
password_path_dsize = (password_path_width, password_path_height)

password_path = cv2.resize(password_path, password_path_dsize, interpolation = cv2.INTER_AREA)

cv2.imwrite("Buttons/password_scaled.png", password_path)

password_path = "Buttons/password_scaled.png"

password = pyautogui.locateCenterOnScreen(password_path, confidence = 0.95)
if password == None:
    scale = int(scale * 1000)
    if scale > 600:
        add_percents = 50
    else:
        add_percents = 100
    for i in range(scale - add_percents, scale + add_percents + 1):
        password_path = cv2.imread("Buttons/password_175.png", cv2.IMREAD_UNCHANGED)

        password_path_width = int(password_path.shape[1] * i / 1000)#
        password_path_height = int(password_path.shape[0] * i / 1000)
        password_path_dsize = (password_path_width, password_path_height)

        password_path = cv2.resize(password_path, password_path_dsize, interpolation = cv2.INTER_AREA)

        cv2.imwrite("Buttons/password_scaled.png", password_path)

        password_path = "Buttons/password_scaled.png"

        if scale > 600:
            password = pyautogui.locateCenterOnScreen(password_path, confidence = 0.85)

            if password:
                scale = i / 1000
                conf = 0.85
                print("2nd scaling success", scale)
                break

        else:
            password = pyautogui.locateCenterOnScreen(password_path, confidence = 0.8)

            if password:
                scale = i / 1000
                conf = 0.75
                print("2nd scaling success", scale)
                break

else:
    conf = 0.85
    print("2nd scaling success", scale)

email_path_width = int(email_path.shape[1] * scale)#
email_path_height = int(email_path.shape[0] * scale)
email_path_dsize = (email_path_width, email_path_height)
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
sms_code_form_check_path_width = int(sms_code_form_check_path.shape[1] * scale)#
sms_code_form_check_path_height = int(sms_code_form_check_path.shape[0] * scale)
sms_code_form_check_path_dsize = (sms_code_form_check_path_width, sms_code_form_check_path_height)

email_path = cv2.resize(email_path, email_path_dsize, interpolation = cv2.INTER_AREA)
login_path = cv2.resize(login_path, login_path_dsize, interpolation = cv2.INTER_AREA)
captcha_path = cv2.resize(captcha_path, captcha_path_dsize, interpolation = cv2.INTER_AREA)
get_sms_code_path = cv2.resize(get_sms_code_path, get_sms_code_path_dsize, interpolation = cv2.INTER_AREA)
sms_check_path = cv2.resize(sms_check_path, sms_check_path_dsize, interpolation = cv2.INTER_AREA)
sms_path = cv2.resize(sms_path, sms_path_dsize, interpolation = cv2.INTER_AREA)
sms_code_form_path = cv2.resize(sms_code_form_path, sms_code_form_path_dsize, interpolation = cv2.INTER_AREA)
sms_code_form_check_path = cv2.resize(sms_code_form_check_path, sms_code_form_check_path_dsize, interpolation = cv2.INTER_AREA)

cv2.imwrite("Buttons/email_scaled.png", email_path)
cv2.imwrite("Buttons/login_scaled.png", login_path)
cv2.imwrite("Buttons/captcha_scaled.png", captcha_path)
cv2.imwrite("Buttons/get_sms_code_scaled.png", get_sms_code_path)
cv2.imwrite("Buttons/sms_check_scaled.png", sms_check_path)
cv2.imwrite("Buttons/sms_scaled.png", sms_path)
cv2.imwrite("Buttons/sms_code_form_scaled.png", sms_code_form_path)
cv2.imwrite("Buttons/sms_code_form_check_scaled.png", sms_code_form_check_path)

email_path = "Buttons/email_scaled.png"
login_path = "Buttons/login_scaled.png"
captcha_path = "Buttons/captcha_scaled.png"
get_sms_code_path = "Buttons/get_sms_code_scaled.png"
sms_check_path = "Buttons/sms_check_scaled.png"
sms_path = "Buttons/sms_scaled.png"
sms_code_form_path = "Buttons/sms_code_form_scaled.png"
sms_code_form_check_path = "Buttons/sms_code_form_check_scaled.png"

email = pyautogui.locateCenterOnScreen(email_path, confidence = conf)
while email == None:
    pyautogui.sleep(0.1)
    email = pyautogui.locateCenterOnScreen(email_path, confidence = conf)
ahk.click(email)
print("email success")
ahk.type("")

ahk.click(password)
print("password success")
ahk.type("")

login = pyautogui.locateCenterOnScreen(login_path, confidence = conf)
while login == None:
    pyautogui.sleep(0.1)
    login = pyautogui.locateCenterOnScreen(login_path, confidence = conf)
ahk.click(login)
print("login success")

captcha = pyautogui.locateCenterOnScreen(captcha_path, confidence = conf - 0.05)
while captcha == None:
    pyautogui.sleep(0.1)
    captcha = pyautogui.locateCenterOnScreen(captcha_path, confidence = conf - 0.05)
ahk.mouse_move(captcha[0], captcha[1])
print("captcha success")

get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = conf - 0.05)
while get_sms_code == None:
    pyautogui.sleep(0.1)
    get_sms_code = pyautogui.locateCenterOnScreen(get_sms_code_path, confidence = conf - 0.05)
ahk.click(get_sms_code)
print("get_sms_code success")

webbrowser.open_new("https://messages.google.com/web/conversations/54")

sms_check = pyautogui.locateCenterOnScreen(sms_check_path, confidence = conf - 0.05)
while sms_check == None:
    pyautogui.sleep(0.1)
    sms_check = pyautogui.locateCenterOnScreen(sms_check_path, confidence = conf - 0.05)
if sms_check:
    print("sms_check success")
    pyautogui.sleep(0.1)
    sms = list(pyautogui.locateAllOnScreen(sms_path, confidence = conf - 0.05))
    while sms == None:
        pyautogui.sleep(0.1)
        sms = list(pyautogui.locateAllOnScreen(sms_path, confidence = conf - 0.05))
    sms = sms[-1]
    sms = pyautogui.screenshot(region=(sms))
    print("sms success")
    pyautogui.sleep(0.1)
sms_text = pytesseract.image_to_string(sms)
sms_code = str(sms_text.split()[3])
sms_code = sms_code.replace(".", "")
sms_code = sms_code.strip()

ahk.send_event("^w")

if scale <= 0.6 :
    ahk.double_click(light_theme_switch)

sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = conf - 0.1)
while sms_code_form == None:
    pyautogui.sleep(0.1)
    sms_code_form = pyautogui.locateCenterOnScreen(sms_code_form_path, confidence = conf - 0.1)
ahk.click(sms_code_form)
print("sms_code_form success")

ahk.type(sms_code)

sms_code_form_check = pyautogui.locateCenterOnScreen(sms_code_form_check_path, confidence = conf)
while sms_code_form_check == None:
    pyautogui.sleep(0.1)
    sms_code_form_check = pyautogui.locateCenterOnScreen(sms_code_form_check_path, confidence = conf)
print("sms_code_form_check success")

ahk.send_event("^l")
pyautogui.sleep(0.1)
ahk.type("https://www.binance.com/ru/trade/BTC_USDT?layout=basic")
pyautogui.sleep(0.1)
ahk.send_event("{Enter}")
print("trading page")

stop = ahk.key_state("Esc")
while stop == False:
    price = driver.find_element_by_class_name("showPrice").text
    print(price)
    stop = ahk.key_state("Esc")
    pyautogui.sleep(0.1)
