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

EMAIL = ""
PASSWORD = ""
SMS_LINK = ""
USED_PERCENT_OF_BALANCE = 66 / 100

start = datetime.now()
timeout = start + timedelta(seconds = 10)

ahk = AHK()
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

dark_theme_switch_path = "Buttons/dark_theme_switch_175.png"
light_theme_switch_path = "Buttons/light_theme_switch_175.png"

buttons = {
    "email" : "Buttons/email_175.png",
    "login" : "Buttons/login_175.png",
    "captcha" : "Buttons/captcha_175.png",
    "get_sms_code" : "Buttons/get_sms_code_175.png",
    "sms_check" : "Buttons/sms_check_175.png",
    "sms" : "Buttons/sms_175.png",
    "sms_code_form" : "Buttons/sms_code_form_175.png",
    "sms_code_form_check" : "Buttons/sms_code_form_check_175.png",
    "search" : "Buttons/search_175.png",
    "buy_location" : "Buttons/buy_location_175.png",
    "sell_location" : "Buttons/sell_location_175.png",
    "price" : "Buttons/price_175.png",
    "quantity" : "Buttons/quantity_175.png",
    "quantity_form" : "Buttons/quantity_form_175.png",
    "cost" : "Buttons/cost_175.png",
    "buy_button" : "Buttons/buy_button_175.png",
    "sell_button" : "Buttons/sell_button_175.png"
    }
dsize = {
    "email" : "",
    "login" : "",
    "captcha" : "",
    "get_sms_code" : "",
    "sms_check" : "",
    "sms" : "",
    "sms_code_form" : "",
    "sms_code_form_check" : "",
    "search" : "",
    "buy_location" : "",
    "sell_location" : "",
    "price" : "",
    "quantity" : "",
    "quantity_form" : "",
    "cost" : "",
    "buy_button" : "",
    "sell_button" : "",
    }

webbrowser.open_new("https://accounts.binance.com/ru/login")

driver = webdriver.Chrome("D:/Документы/Python/Autoclicker_test/Chromedriver/chromedriver.exe", chrome_options = options)

driver.get("https://www.binance.com/ru/trade/BTC_USDT?layout=basic")
pyautogui.sleep(0.5)

browser = ahk.active_window 
browser.maximize()

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

password_path = cv2.imread("Buttons/password_175.png", cv2.IMREAD_UNCHANGED)

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

for i, value in buttons.items():
    buttons[i] = cv2.imread(buttons[i], cv2.IMREAD_UNCHANGED)

    dsize[i] = (int(buttons[i].shape[1] * scale), int(buttons[i].shape[0] * scale))

    img = cv2.resize(buttons[i], dsize[i], interpolation = cv2.INTER_AREA)

    cv2.imwrite("Buttons/" + i + "_scaled.png", img)

    buttons[i] = "Buttons/" + i + "_scaled.png"

email = pyautogui.locateCenterOnScreen(buttons["email"], confidence = conf)
while email == None:
    pyautogui.sleep(0.1)
    email = pyautogui.locateCenterOnScreen(buttons["email"], confidence = conf)
ahk.click(email)
print("email success")
ahk.type(EMAIL)

ahk.click(password)
print("password success")
ahk.type(PASSWORD)

login = pyautogui.locateCenterOnScreen(buttons["login"], confidence = conf)
while login == None:
    pyautogui.sleep(0.1)
    login = pyautogui.locateCenterOnScreen(buttons["login"], confidence = conf)
ahk.click(login)
print("login success")

captcha = pyautogui.locateCenterOnScreen(buttons["captcha"], confidence = conf - 0.05)
while captcha == None:
    pyautogui.sleep(0.1)
    captcha = pyautogui.locateCenterOnScreen(buttons["captcha"], confidence = conf - 0.05)
ahk.mouse_move(captcha[0], captcha[1])
print("captcha success")

get_sms_code = pyautogui.locateCenterOnScreen(buttons["get_sms_code"], confidence = conf - 0.05)
while get_sms_code == None:
    pyautogui.sleep(0.1)
    get_sms_code = pyautogui.locateCenterOnScreen(buttons["get_sms_code"], confidence = conf - 0.05)
ahk.click(get_sms_code)
print("get_sms_code success")

webbrowser.open_new(SMS_LINK)

sms_check = pyautogui.locateCenterOnScreen(buttons["sms_check"], confidence = conf - 0.05)
while sms_check == None:
    pyautogui.sleep(0.1)
    sms_check = pyautogui.locateCenterOnScreen(buttons["sms_check"], confidence = conf - 0.05)
if sms_check:
    print("sms_check success")
    pyautogui.sleep(0.1)
    sms = list(pyautogui.locateAllOnScreen(buttons["sms"], confidence = conf - 0.05))
    while sms == None:
        pyautogui.sleep(0.1)
        sms = list(pyautogui.locateAllOnScreen(buttons["sms"], confidence = conf - 0.05))
    sms = sms[-1]
    sms = pyautogui.screenshot(region = (sms))
    print("sms success")
    pyautogui.sleep(0.1)
sms_text = pytesseract.image_to_string(sms)
sms_code = str(sms_text.split()[3])
sms_code = sms_code.replace(".", "")
sms_code = sms_code.strip()

ahk.send_event("^w")

if scale <= 0.6 :
    ahk.double_click(light_theme_switch)

sms_code_form = pyautogui.locateCenterOnScreen(buttons["sms_code_form"], confidence = conf - 0.1)
while sms_code_form == None:
    pyautogui.sleep(0.1)
    sms_code_form = pyautogui.locateCenterOnScreen(buttons["sms_code_form"], confidence = conf - 0.1)
ahk.click(sms_code_form)
print("sms_code_form success")

ahk.type(sms_code)

sms_code_form_check = pyautogui.locateCenterOnScreen(buttons["sms_code_form_check"], confidence = conf)
while sms_code_form_check == None:
    pyautogui.sleep(0.1)
    sms_code_form_check = pyautogui.locateCenterOnScreen(buttons["sms_code_form_check"], confidence = conf)
print("sms_code_form_check success")

ahk.send_event("^l")
pyautogui.sleep(0.1)
ahk.type("https://www.binance.com/ru/trade/ETH_USDT?layout=basic")
pyautogui.sleep(0.1)
ahk.send_event("{Enter}")
pyautogui.sleep(0.1)
search = pyautogui.locateCenterOnScreen(buttons["search"], confidence = conf)
while search == None:
    pyautogui.sleep(0.1)
    search = pyautogui.locateCenterOnScreen(buttons["search"], confidence = conf)
pyautogui.sleep(0.1)
ahk.send_event("{Space}")
print("trading page")

class buy:
    location = pyautogui.locateOnScreen(buttons["buy_location"], confidence = conf)
    while location == None:
        pyautogui.sleep(0.1)
        location= pyautogui.locateOnScreen(buttons["buy_location"], confidence = conf)
    price = pyautogui.locateCenterOnScreen(buttons["price"], region = (location), confidence = conf - 0.05)
    quantity = pyautogui.locateOnScreen(buttons["quantity"], region = (location), confidence = conf - 0.05)
    quantity_form = pyautogui.locateOnScreen(buttons["quantity_form"], region = (location), confidence = conf - 0.05)
    quantity_value = 0
    cost = pyautogui.locateCenterOnScreen(buttons["cost"], region = (location), confidence = conf - 0.05)
    button = pyautogui.locateCenterOnScreen(buttons["buy_button"], confidence = conf)
class sell:
    location = pyautogui.locateOnScreen(buttons["sell_location"], confidence = conf)
    while location == None:
        pyautogui.sleep(0.1)
        location= pyautogui.locateOnScreen(buttons["sell_location"], confidence = conf)
    price = pyautogui.locateCenterOnScreen(buttons["price"], region = (location), confidence = conf - 0.05)
    quantity = pyautogui.locateOnScreen(buttons["quantity"], region = (location), confidence = conf - 0.05)
    quantity_value = 0
    quantity_form = pyautogui.locateOnScreen(buttons["quantity_form"], region = (location), confidence = conf - 0.05)
    cost = pyautogui.locateCenterOnScreen(buttons["cost"], region = (location), confidence = conf - 0.05)
    button = pyautogui.locateCenterOnScreen(buttons["sell_button"], confidence = conf)

pyautogui.sleep(0.1)
ahk.click(buy.quantity[0] + buy.quantity[2] * USED_PERCENT_OF_BALANCE, buy.quantity[1] + buy.quantity[3] * 0.5)
pyautogui.sleep(0.1)

buy.quantity_value = pyautogui.screenshot(region = (buy.quantity_form[0] + buy.quantity_form[2] * 0.22, buy.quantity_form[1], buy.quantity_form[2] * 0.7, buy.quantity_form[3]))
pyautogui.sleep(0.1)
buy.quantity_value = pytesseract.image_to_string(buy.quantity_value)
buy.quantity_value = str(buy.quantity_value)
buy.quantity_value = buy.quantity_value.replace(",", ".")
buy.quantity_value = buy.quantity_value.strip()
buy.quantity_value = float(buy.quantity_value)
print(buy.quantity_value)

#stop = ahk.key_state("Esc")
#while stop == False:
#    price = driver.find_element_by_class_name("showPrice").text
#    print(price)
#    stop = ahk.key_state("Esc")
#    pyautogui.sleep(0.1)
