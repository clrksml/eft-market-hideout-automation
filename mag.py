# Name: EFT Mag Loader
# Author: Clark
# Website: wwww.HavocGamers.net

import time
import keyboard
import pyautogui

w, h = pyautogui.size()
x, y = pyautogui.position()
loop, count, key = 5, 2, 5
x2, y2 = x, y

def print_xy():
    print(pyautogui.position())
keyboard.add_hotkey('shift+3', print_xy)

def math_clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def increase_loop():
    global loop
    print(loop)
    if loop >= 50:
        loop = 1
    else:
        loop = math_clamp(loop + 1, 1, 50)
    print(loop)
#keyboard.add_hotkey('shift+1', increase_loop)

def increase_count():
    global count
    print(count)
    if count >= 50:
        count = 1
    else:
        count = math_clamp(count + 1, 1, 50)
    print(count)
#keyboard.add_hotkey('shift+2', increase_count)

def load_mags():
    for x in range(0, loop):
                # stack one
                pyautogui.click()
                pyautogui.keyDown('ctrlleft')
                pyautogui.drag(64, 0, 1, button='left')
                pyautogui.keyUp('ctrlleft')
                pyautogui.move(155, 18)
                pyautogui.click()
                pyautogui.press('right')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press(count)
                pyautogui.press('delete')
                pyautogui.press('enter')
                pyautogui.move(-155, -18)
                pyautogui.click()
                pyautogui.drag(64, 0, 0.2, button='left')
                pyautogui.move(-128, 64)

                # stack two
                pyautogui.click()
                pyautogui.keyDown('ctrlleft')
                pyautogui.drag(64, 0, 1, button='left')
                pyautogui.keyUp('ctrlleft')
                pyautogui.move(155, 18)
                pyautogui.click()
                pyautogui.press('right')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press(count)
                pyautogui.press('delete')
                pyautogui.press('enter')
                pyautogui.move(-155, -18)
                pyautogui.click()
                pyautogui.drag(64, 0, 0.2, button='left')
                pyautogui.move(-128, -64)
keyboard.add_hotkey('ctrl+shift+f1', load_mags)
keyboard.wait('alt+w')