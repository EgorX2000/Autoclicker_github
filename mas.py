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

buttons = {"email" : "Buttons/email_175.png", "login" : "Buttons/login_175.png", "captcha" : "Buttons/captcha_175.png", "get_sms_code" : "Buttons/get_sms_code_175.png", "sms_check" : "Buttons/sms_check_175.png", "sms" : "Buttons/sms_175.png", "sms_code_form" : "Buttons/sms_code_form_175.png", "sms_code_form_check" : "Buttons/sms_code_form_check_175.png"}
dsize = {"email" : "", "login" : "", "captcha" : "", "get_sms_code" : "", "sms_check" : "", "sms" : "", "sms_code_form" : "", "sms_code_form_check" : ""}

scale = 0.58

for i, value in buttons.items():
    buttons[i] = cv2.imread(buttons[i], cv2.IMREAD_UNCHANGED)

    dsize[i] = (int(buttons[i].shape[1] * scale), int(buttons[i].shape[0] * scale))

    img = cv2.resize(buttons[i], dsize[i], interpolation = cv2.INTER_AREA)

    cv2.imwrite("Buttons/" + i + "_scaled.png", img)

    buttons[i] = "Buttons/" + i + "_scaled.png"
    print(buttons["email"])