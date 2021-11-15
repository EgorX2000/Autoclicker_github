from datetime import datetime, timedelta
import webbrowser
from ahk import AHK
import cv2
import pyautogui
import pytesseract
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from binance.client import Client
import random
import colorama
from colorama import Fore, Style
colorama.init()

EMAIL = "ebkrivoshapkin@gmail.com"
PASSWORD = "1Qaz2Wsx3Edc4Rfv5Tgb6Yhn7Ujm8Ik,9Ol.0P;/"
API_KEY, API_SECRET = "bKHfCOE3GD8z7GkKciYzAjI39AHjLPQ13cWsD1sZmkM7NoI8DRgMRoxGzy1KnssP", "Ao05qI3wtE0WkAS0F83iZU1X7PZclshgEvCOTtYUJ0Lh4UIRaen0YH2K36pb5KK7"
SMS_LINK = "https://messages.google.com/web/conversations/54"
TRADING_LINK = "https://www.binance.com/ru/trade/ETH_USDT?layout=basic"
USED_PERCENT_OF_BALANCE = 99 / 100

ahk = AHK()
ahk.mouse_speed = 2
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service("D:/Документы/Python/Autoclicker/Chromedriver/chromedriver.exe")

def STOP():
    stop = ahk.key_state("Esc")
    if stop == True:
        driver.quit()
        ahk.send_event("^+w")
        exit()

with open("operation_logs.log", "r") as log:
    length = len(log.readline())
    if length > 0:
        last_and_number = log.readlines()[-8:-5]
        operation_number = int(last_and_number[0].replace("operation #", "").replace("\n", ""))
        last_operation = last_and_number[1].replace("[", "").replace("]:\n", "")
        lastopprice = float(last_and_number[2].replace("    PRICE: ", "").replace("USDT", "").replace("\n", ""))
        if last_operation == "BUY":
            next_operation = "SELL"
        else:
            next_operation = "BUY"
    else:
        operation_number = 0
        next_operation = "BUY"
        lastopprice = 0

dark_theme_switch_path = "Buttons/dark_theme_switch_175.png"
light_theme_switch_path = "Buttons/light_theme_switch_175.png"

buttons = {
    "email" : "Buttons/email_175.png",
    "login" : "Buttons/login_175.png",
    "captcha" : "Buttons/captcha_175.png",
    "captcha_button" : "Buttons/captcha_button_175.png",
    "get_sms_code" : "Buttons/get_sms_code_175.png",
    "sms_check" : "Buttons/sms_check_175.png",
    "sms" : "Buttons/sms_175.png",
    "sms_code_form" : "Buttons/sms_code_form_175.png",
    "sms_code_form_check" : "Buttons/sms_code_form_check_175.png",
    "ad" : "Buttons/ad_175.png",
    "buy_sell_form" : "Buttons/buy_sell_form_175.png",
    "market" : "Buttons/market_175.png",
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
    "captcha_button" : "",
    "get_sms_code" : "",
    "sms_check" : "",
    "sms" : "",
    "sms_code_form" : "",
    "sms_code_form_check" : "",
    "ad" : "",
    "buy_sell_form" : "",
    "market" : "",
    "buy_location" : "",
    "sell_location" : "",
    "price" : "",
    "quantity" : "",
    "quantity_form" : "",
    "cost" : "",
    "buy_button" : "",
    "sell_button" : ""
    }

#font
green = f"{Fore.GREEN}"
red = f"{Fore.RED}"
blue = f"{Fore.CYAN}"
reset = f"{Style.RESET_ALL}"

client = Client(API_KEY, API_SECRET)
client.API_URL = "https://api.binance.com/api"

webbrowser.open_new("https://accounts.binance.com/ru/login")

driver = webdriver.Chrome(service = service, options = options)
driver.get(TRADING_LINK)

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
            ahk.mouse_move(dark_theme_switch[0], dark_theme_switch[1])
            ahk.click()
            print("1st scaling success", scale)
            print("dark_theme_switch success")
            break
        
        elif light_theme_switch:
            scale = i / 100
            print("1st scaling success", scale)
            break

        STOP()
        
elif dark_theme_switch:
    scale = 1
    conf = 0.85
    ahk.mouse_move(dark_theme_switch[0], dark_theme_switch[1])
    ahk.click()
    print("scaling success", scale)

else:
    scale = 1
    conf = 0.85
    print("scaling success", scale)

STOP()

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

        STOP()

else:
    conf = 0.85
    print("2nd scaling success", scale)

STOP()

for i, value in buttons.items():
    buttons[i] = cv2.imread(buttons[i], cv2.IMREAD_UNCHANGED)

    dsize[i] = (int(buttons[i].shape[1] * scale), int(buttons[i].shape[0] * scale))

    img = cv2.resize(buttons[i], dsize[i], interpolation = cv2.INTER_AREA)

    cv2.imwrite("Buttons/" + i + "_scaled.png", img)

    buttons[i] = "Buttons/" + i + "_scaled.png"

def BUTTON(b, conf):
    button = pyautogui.locateOnScreen(buttons[b], confidence = conf)
    while button == None:
        pyautogui.sleep(0.1)
        button = pyautogui.locateOnScreen(buttons[b], confidence = conf)
        STOP()
    STOP()
    return button

def CLICK(b, conf):
    button = pyautogui.locateOnScreen(buttons[b], confidence = conf)
    while button == None:
        pyautogui.sleep(0.1)
        button = pyautogui.locateOnScreen(buttons[b], confidence = conf)
        STOP()
    ahk.mouse_move(button[0] + button[2] * 0.5, button[1] + button[3] * 0.5)
    pyautogui.sleep(0.01)
    ahk.click()
    STOP()
    return button

def LOGIN():
    global email, login, captcha
    
    email = CLICK("email", conf)
    ahk.type(str(EMAIL))

    ahk.mouse_move(password[0], password[1])
    pyautogui.sleep(0.01)
    ahk.click()
    ahk.type(str(PASSWORD))

    login = CLICK("login", conf)

    captcha = BUTTON("captcha", conf)
    ahk.mouse_move(captcha[0] + captcha[2] * 0.07, captcha[1] + captcha[3] * 0.5)
    ahk.mouse_drag(random.randint(int(captcha[0] + captcha[2] * 0.26), int(captcha[0] + captcha[2] * 0.93)), captcha[1] + captcha[3] * 0.5)
    pyautogui.sleep(2)
    STOP()
    captcha_button = pyautogui.locateOnScreen(buttons["captcha_button"], confidence = conf - 0.05)
    if captcha_button != None:
        ahk.send_event("^+r")
        LOGIN()
    else:
        print("login&captcha success")
        return

LOGIN()

get_sms_code = CLICK("get_sms_code", conf - 0.05)
print("get_sms_code success")

webbrowser.open_new(SMS_LINK)

sms_check = BUTTON("sms_check", conf - 0.05)
print("sms_check success")
pyautogui.sleep(0.1)
sms = list(pyautogui.locateAllOnScreen(buttons["sms"], confidence = conf - 0.05))
while sms == None:
    pyautogui.sleep(0.1)
    sms = list(pyautogui.locateAllOnScreen(buttons["sms"], confidence = conf - 0.05))
    STOP()
sms = sms[-1]
sms = pyautogui.screenshot(region = (sms))
print("sms success")
pyautogui.sleep(0.1)
sms_text = pytesseract.image_to_string(sms)
sms_code = sms_text.split()[3]
sms_code = sms_code.replace(".", "").strip()

ahk.send_event("^w")

sms_code_form = CLICK("sms_code_form", conf - 0.1)
print("sms_code_form success")

ahk.type(str(sms_code))
pyautogui.sleep(0.5)
ahk.send_event("{Enter}")

sms_code_form_check = BUTTON("sms_code_form_check", conf - 0.05)
print("sms_code_form_check success")

ahk.mouse_speed = 0

ahk.send_event("^l")
pyautogui.sleep(0.1)
ahk.type(str(TRADING_LINK))
pyautogui.sleep(0.1)
ahk.send_event("{Enter}")
pyautogui.sleep(0.1)
ahk.mouse_move(0, 100)
pyautogui.sleep(0.1)
start = datetime.now()
timeout = start + timedelta(seconds = 120)
ad = pyautogui.locateOnScreen(buttons["ad"], confidence = conf - 0.05)
while ad == None and start < timeout:
    pyautogui.sleep(0.1)
    ad = pyautogui.locateOnScreen(buttons["ad"], confidence = conf - 0.05)
    start = datetime.now()
    STOP()
pyautogui.sleep(0.1)
buy_sell_form = pyautogui.locateOnScreen(buttons["buy_sell_form"], confidence = conf)
while buy_sell_form == None:
    pyautogui.sleep(0.1)
    ahk.wheel_down()
    buy_sell_form = pyautogui.locateOnScreen(buttons["buy_sell_form"], confidence = conf)
    STOP()
ahk.mouse_move(0, 0)
pyautogui.sleep(0.1)
market = pyautogui.locateOnScreen(buttons["market"], region = (buy_sell_form), confidence = conf - 0.15)
ahk.mouse_move(market[0] + market[2] * 0.5, market[1] + market[3] * 0.5)
pyautogui.sleep(0.01)
ahk.click()
print("trading page")

class buy:
    location = BUTTON("buy_location", conf)
    price = pyautogui.locateCenterOnScreen(buttons["price"], region = (location), confidence = conf - 0.05)
    quantity = pyautogui.locateOnScreen(buttons["quantity"], region = (location), confidence = conf - 0.1)
    quantity_form = pyautogui.locateCenterOnScreen(buttons["quantity_form"], region = (location), confidence = conf - 0.05)
    max_quantity = 0
    cost = pyautogui.locateCenterOnScreen(buttons["cost"], region = (location), confidence = conf)
    button = pyautogui.locateCenterOnScreen(buttons["buy_button"], confidence = conf)
class sell:
    location = BUTTON("sell_location", conf)
    price = pyautogui.locateCenterOnScreen(buttons["price"], region = (location), confidence = conf - 0.05)
    quantity = pyautogui.locateOnScreen(buttons["quantity"], region = (location), confidence = conf - 0.1)
    max_quantity = 0
    quantity_form = pyautogui.locateCenterOnScreen(buttons["quantity_form"], region = (location), confidence = conf - 0.05)
    cost = pyautogui.locateCenterOnScreen(buttons["cost"], region = (location), confidence = conf)
    button = pyautogui.locateCenterOnScreen(buttons["sell_button"], confidence = conf)

def INFO(operation_number, price, quantity, reason, operation, color):
    pyautogui.sleep(2.5)
    balance = BALANCE(price)

    info = f'''{datetime.now().replace(microsecond=0)}
$blueoperation #{operation_number}
$color[$operation]:
    PRICE: {price} USDT
    QUANTITY: {quantity} ETH
    COST: {round(price * quantity, 2)} USDT
    REASON: {reason}
BALANCE: {balance} USDT$reset

'''

    print(info.replace("$operation", operation).replace("$color", color).replace("$blue", blue).replace("$reset", reset))

    with open("operation_logs.log", "a") as log:
        log.write(info.replace("$operation", operation).replace("$color", "").replace("$blue", "").replace("$reset", ""))

def BALANCE(price):
    usdt = float(client.get_asset_balance(asset="USDT")["free"]) + float(client.get_asset_balance(asset="USDT")["locked"])
    eth = float(client.get_asset_balance(asset="ETH")["free"]) + float(client.get_asset_balance(asset="ETH")["locked"])
    eth2usdt = eth * price
    balance = round(usdt + eth2usdt, 2)
    return balance

def BUY(price, operation_number, reason):
    ahk.mouse_move(buy.quantity[0] + buy.quantity[2], buy.quantity[1] + buy.quantity[3] * 0.5)
    pyautogui.sleep(0.01)
    ahk.click()
    pyautogui.sleep(0.01)

    ahk.mouse_move(buy.quantity_form[0], buy.quantity_form[1])
    pyautogui.sleep(0.01)
    ahk.click()
    pyautogui.sleep(0.01)
    ahk.send_event("^a")
    pyautogui.sleep(0.01)
    ahk.send_event("^c")
    pyautogui.sleep(0.01)
    buy.max_quantity = str(pyperclip.paste())
    buy.max_quantity = float(buy.max_quantity.replace(",", "."))
    ahk.mouse_move(buy.quantity_form[0], buy.quantity_form[1])
    pyautogui.sleep(0.01)
    ahk.click()

    quantity = round(buy.max_quantity * USED_PERCENT_OF_BALANCE, 4)

    if quantity >= 11 / price:
        ahk.mouse_move(buy.quantity_form[0], buy.quantity_form[1])
        pyautogui.sleep(0.01)
        ahk.click()
        pyautogui.sleep(0.01)
        ahk.send_event("^a")
        pyautogui.sleep(0.01)
        ahk.type(str(quantity).replace(".", ","))
        pyautogui.sleep(0.01)

        ahk.mouse_move(buy.button[0], buy.button[1])
        pyautogui.sleep(0.01)
        ahk.double_click()
        pyautogui.sleep(0.1)
        ahk.mouse_move(0,0)

        INFO(operation_number, price, quantity, reason, operation = "BUY", color = f"{green}")

        return(price)
    
    else:
        return

def SELL(price, operation_number, reason):
    ahk.mouse_move(sell.quantity[0] + sell.quantity[2], sell.quantity[1] + sell.quantity[3] * 0.5)
    pyautogui.sleep(0.01)
    ahk.click()
    pyautogui.sleep(0.01)

    ahk.mouse_move(sell.quantity_form[0], sell.quantity_form[1])
    pyautogui.sleep(0.01)
    ahk.click()
    pyautogui.sleep(0.01)
    ahk.send_event("^a")
    pyautogui.sleep(0.01)
    ahk.send_event("^c")
    pyautogui.sleep(0.01)
    sell.max_quantity = str(pyperclip.paste())
    sell.max_quantity = float(sell.max_quantity.replace(",", "."))
    ahk.mouse_move(sell.quantity_form[0], sell.quantity_form[1])
    pyautogui.sleep(0.01)
    ahk.click()

    quantity = round(sell.max_quantity * USED_PERCENT_OF_BALANCE, 4)

    if quantity >= 11 / price:
        ahk.mouse_move(sell.quantity_form[0], sell.quantity_form[1])
        pyautogui.sleep(0.01)
        ahk.click()
        pyautogui.sleep(0.01)
        ahk.send_event("^a")
        pyautogui.sleep(0.01)
        ahk.type(str(quantity).replace(".", ","))
        pyautogui.sleep(0.01)

        ahk.mouse_move(sell.button[0], sell.button[1])
        pyautogui.sleep(0.01)
        ahk.double_click()
        pyautogui.sleep(0.1)
        ahk.mouse_move(0,0)

        INFO(operation_number, price, quantity, reason, operation = "SELL", color = f"{red}")

        return(price)
    
    else:
        return

buy_success = False
sell_success = False
ahk.mouse_move(buy.quantity[0], buy.quantity[1] + buy.quantity[3] * 0.5)
pyautogui.sleep(0.01)
ahk.click()
pyautogui.sleep(0.1)
ahk.mouse_move(0,0)
if lastopprice == 0:
    price = float(driver.find_element(By.CLASS_NAME, "showPrice").text.replace(",", ""))
    lastopprice = price
start = datetime.now()
timeout = start + timedelta(seconds = 600)
stop = ahk.key_state("Esc")
while stop == False:
    start = datetime.now()
    if start >= timeout:
        ahk.mouse_move(0,0)
        timeout = start + timedelta(seconds = 600)

    #buy thresholds
    dip_threshold = -0.3
    upward_trend_threshold = 0.35

    #sell thresholds
    profit_threshold = 0.325
    stop_loss_threshold = -0.375

    price = float(driver.find_element(By.CLASS_NAME, "showPrice").text.replace(",", ""))

    percentageDiff = (price - lastopprice) / lastopprice * 100

    if next_operation == "BUY":
        if percentageDiff <= dip_threshold:
            threshold_price = price
            print(threshold_price, datetime.now().replace(microsecond=0))
            tolerance = 5
            tolerance_start = datetime.now()
            tolerance_timeout = tolerance_start + timedelta(seconds = 5)
            while price <= threshold_price + tolerance:
                if tolerance_start >= tolerance_timeout:
                    tolerance = 2.5
                price = float(driver.find_element(By.CLASS_NAME, "showPrice").text.replace(",", ""))
                if price <= threshold_price - 0.1:
                    threshold_price = price
                tolerance_start = datetime.now()
                STOP()
            else:
                operation_number += 1
                reason = "DIP_THRESHOLD"
                lastopprice = BUY(price, operation_number, reason)
                buy_success = True
                pyautogui.sleep(5)
                if lastopprice == None:
                    operation_number -= 1
                    lastopprice = price

        elif percentageDiff >= upward_trend_threshold:
            operation_number += 1
            reason = "UPWARD_TREND_THRESHOLD"
            lastopprice = BUY(price, operation_number, reason)
            buy_success = True
            pyautogui.sleep(5)
            if lastopprice == None:
                    operation_number -= 1
                    lastopprice = price

    if next_operation == "SELL":
        if percentageDiff >= profit_threshold:
            threshold_price = price
            print(threshold_price, datetime.now().replace(microsecond=0))
            tolerance = 5
            tolerance_start = datetime.now()
            tolerance_timeout = tolerance_start + timedelta(seconds = 5)
            while price >= threshold_price - tolerance:
                if tolerance_start >= tolerance_timeout:
                    tolerance = 2.5
                price = float(driver.find_element(By.CLASS_NAME, "showPrice").text.replace(",", ""))
                if price >= threshold_price + 0.1:
                    threshold_price = price
                tolerance_start = datetime.now()
                STOP()
            else:
                operation_number += 1
                reason = "PROFIT_THRESHOLD"
                lastopprice = SELL(price, operation_number, reason)
                sell_success = True
                pyautogui.sleep(5)
                if lastopprice == None:
                    operation_number -= 1
                    lastopprice = price

        elif percentageDiff <= stop_loss_threshold:
            operation_number += 1
            reason = "STOP_LOSS_THRESHOLD"
            lastopprice = SELL(price, operation_number, reason)
            sell_success = True
            pyautogui.sleep(5)
            if lastopprice == None:
                    operation_number -= 1
                    lastopprice = price

    if buy_success == True:
        next_operation = "SELL"
        buy_success = False

    elif sell_success == True:
        next_operation = "BUY"
        sell_success = False

    stop = ahk.key_state("Esc")
else:
    driver.quit()
    ahk.send_event("^+w")
    exit()