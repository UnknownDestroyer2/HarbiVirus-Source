import pyautogui
import random
import time

screen_width, screen_height = pyautogui.size()
# 15 sn fareyi random ışınla
start_time = time.time()
while time.time() - start_time < 15:
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(x, y, duration=0.0001) 
