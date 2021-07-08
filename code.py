import pyautogui
import random
import time


while True:
    x = random.randint(0,300)
    y = random.randint(0,500)
    pyautogui.moveTo(x,y)
    time.sleep(1)