# Name: EFT Hideout and Trader Automation
# Author: Clark
# Website: www.HavocGamers.net

import os
import time
import keyboard
import pyautogui
import cv2
import random

w, h = pyautogui.size()
x, y = pyautogui.position()
kill = False
tobuy = ['4', '4', '2', '3', '12', '4', '4', '4', '5', '2', '4']
goods = {'A3 Adapter': 5500, 'ST-6012': 19000, 'SubSX': 500, 'BP': 880, 'M855A1': 400, 'SPP': 925, '7BT1': 612, 'APSX': 750,'PDC': 25700, 'M856A1': 380, 'PICBLOCK': 6000, 'MPX Drum': 25000, 'SAI QB Rail': 44000, '57 tr 57x28': 13600, 'JPGS5b': 14000, 'Ergo PSG-1': 31000, 'Shift': 22000, '57x28 57': 4900, 'BS': 950, 'AP63': 700, 'SB193': 335, 'SS190': 600, '7n1': 780, '7n37': 1150, 'LugerCCI': 400, 'M80': 290, 'Grizzly': 54000, 'Allu': 17500 }
traders = ['prapor', 'therapist', 'fence', 'skier', 'peacekeeper', 'mechanic', 'ragman', 'jaeger']
autoselect = False

def msg(s):
    if (kill == True):
        return
    else:
        print(s)

def math_clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)

def sleep( s=0.1 ):
    time.sleep(s)

def click( b='left' ):
    if (kill == True):
        return
    else:
        pyautogui.click(button=b)

def moveto(x, y, s=0):
    if (kill == True):
        return
    else:
        pyautogui.moveTo(x, y, s)

def dragto(x, y, b='left', s=0):
    if (kill == True):
        return
    else:
        pyautogui.dragTo(x, y, s, button=b)

def presskey(k):
    if (kill == True):
        return
    else:
        pyautogui.press(k)

def halt():
    global kill

    if (kill == False):
        msg('Halting.')
        kill = True
    else:
        kill = False
keyboard.add_hotkey('ctrl+shift+f1', halt)

def select_trader( who ):
    if (kill == True):
        return
    else:
        if (who in traders):
            _trader = pyautogui.locateOnScreen('C:/' + who + '.png', confidence=0.80)
            if (_trader) and (_trader[0] > 0) and (_trader[1] > 0):
                sleep(1)
                dragto(_trader[0] + 64, _trader[1] + 64, 'left')
                sleep(2)

def in_stock():
    if (kill == True):
        return
    else:
        _instock = pyautogui.locateOnScreen('C:/instock.png', confidence=0.70)
        if (_instock):
            return True
        else:
            return False

def sell_goods( image, price ):
    if (kill == True):
        return
    else:
        # scroll down
        _max = pyautogui.locateOnScreen('C:/7out7.png', confidence=0.70)
        for x in range(0, 10):
            dragto(1042, 160, 'left')
            sleep(1)

        for x in range(0, 10):
            if (_max):
                msg('Cannot sell anymore items(15 out 15).')
                break
            else:
                presskey('down')
                sleep(1)
                _item = pyautogui.locateOnScreen('C:/' + image + '.png', confidence=0.65)
                if (_item) and (_item[0] > 0) and (_item[1] > 0):
                    sleep(1)
                    # select image
                    dragto(_item[0] + 32, _item[1] + 32, 'left')
                    sleep(1)

                    # open price menu
                    dragto(1464, 430, 'left')
                    sleep(1)
                    _pricewindow = pyautogui.locateOnScreen('C:/pricewindow.png', confidence=0.65)
                    _add = pyautogui.locateOnScreen('C:/add.png', confidence=0.65)
                    _quantity = pyautogui.locateOnScreen('C:/quantity.png', confidence=0.65)
                    _enterprice = pyautogui.locateOnScreen('C:/enterprice.png', confidence=0.65)
                    if (_pricewindow) and (_pricewindow[0] > 0) and (_pricewindow[1] > 0):
                        # price window
                        moveto(_pricewindow[0], _pricewindow[1], 0.2)
                        sleep(1)
                        dragto(_pricewindow[0], _pricewindow[1] - 64, 'left', 2)
                        sleep(1)
                        _add = pyautogui.locateOnScreen('C:/add.png', confidence=0.65)
                        _quantity = pyautogui.locateOnScreen('C:/quantity.png', confidence=0.65)
                        _enterprice = pyautogui.locateOnScreen('C:/enterprice.png', confidence=0.65)
                        sleep(1)

                    if (_enterprice) and (_enterprice[0] > 0) and (_enterprice[1] > 0):
                        # enter price
                        dragto(_enterprice[0], _enterprice[1], 'left')
                        sleep(1)

                        digits = [int(x) for x in str(price)]

                        for s in digits:
                            presskey(str(s))
                            sleep(1)


                        # set price
                        if (_add) and (_add[0] > 0) and (_add[1] > 0):
                            dragto(_add[0] + 50, _add[1] + 64, 'left')
                            sleep(1)

                            # place offer
                            dragto(1283, 817, 'left')
                            msg('Placed ' + image + ' offer on market.')
                            sleep(1)
                            break

                        if (_quantity) and (_quantity[0] > 0) and (_quantity[1] > 0):
                            dragto(_quantity[0] + 120, _quantity[1] + 44, 'left')
                            sleep(1)

                            # place offer
                            dragto(1283, 817, 'left')
                            msg('Placed ' + image + ' offer on market.')
                            sleep(1)
                            break

def collect_bitcoin():
    if (kill == True):
        return
    else:
        # select Bitcoin Farm
        sleep(1)
        dragto(917, 346, 'left')
        sleep(1)
        # grab
        dragto(1593, 740, 'left')
        sleep(1)
        presskey('escape')
        sleep(1)

def collect_workbench():
    if (kill == True):
        return
    else:
        # select Workbench
        moveto(w / 2, h / 2, 0.1)
        sleep(1)
        dragto(568, 215, 'left')
        sleep(5)

        # click scrollbar
        dragto(1888, 195, 'left')
        # scroll down
        for x in range(0, 10):
            presskey('down')
            sleep(1)
            _button = pyautogui.locateOnScreen('C:/getitems.png', confidence=0.6)
            if (_button) and (_button[0] > 0) and (_button[1] > 0):
                # grab
                sleep(1)
                dragto(_button[0], _button[1], 'left')
                sleep(1)
                dragto(_button[0], _button[1], 'left')
                sleep(1)
                # requirements
                presskey('y')
                sleep(1)
                # restart
                dragto(_button[0], _button[1], 'left')
                sleep(1)
                break
        presskey('enter')
        sleep(1)
        presskey('escape')
        sleep(1)

def collect_water():
    if (kill == True):
        return
    else:
        # select Water collector
        moveto(w / 2, h / 2, 0.1)
        sleep(1)
        dragto(1161, 178, 'left')
        sleep(1)
        _button = pyautogui.locateOnScreen('C:/getitems.png', confidence=0.6)
        if (_button) and (_button[0] > 0) and (_button[1] > 0):
            sleep(1)
            # grab
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            # requirements
            dragto(1298, 781, 'left')
            sleep(1)
            presskey('y')
            # restart
            sleep(1)
            dragto(_button[0], _button[1], 'left')
        sleep(1)
        _button = pyautogui.locateOnScreen('C:/start.png', confidence=0.6)
        if (_button) and (_button[0] > 0) and (_button[1] > 0):
            sleep(1)
            # grab
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            # requirements
            _button3 = pyautogui.locateOnScreen('C:/waterfilter.png', confidence=0.6)
            if (_button3) and (_button3[0] > 0) and (_button3[1] > 0):
                sleep(1)
                dragto(_button3[0] + 16, _button3[1] + 32, 'left')
                sleep(1)
            sleep(1)
            # restart
            sleep(1)
            dragto(_button[0], _button[1], 'left')

        _button2 = pyautogui.locateOnScreen('C:/nowater.png', confidence=0.6)
        if (_button2) and (_button2[0] > 0) and (_button2[1] > 0):
            dragto(_button2[0] + 72, _button2[1] + 16, 'left')
            sleep(1)
            _button3 = pyautogui.locateOnScreen('C:/waterfilter.png', confidence=0.6)
            if (_button3) and (_button3[0] > 0) and (_button3[1] > 0):
                dragto(_button3[0] + 16, _button3[1] + 32, 'left')
                sleep(1)
        sleep(1)
        presskey('escape')
        sleep(1)

def collect_scavcase():
    if (kill == True):
        return
    else:
        # scav case
        dragto(1401, 911, 'left')
        sleep(1)
        _getitems = pyautogui.locateOnScreen('C:/getitems.png', confidence=0.6)
        if (_getitems) and (_getitems[0] > 0) and (_getitems[1] > 0):
            sleep(1)
            # grab
            dragto(_getitems[0], _getitems[1], 'left')
            sleep(1)
            dragto(_getitems[0], _getitems[1], 'left')
            sleep(1)
            # receive
            _receive = pyautogui.locateOnScreen('C:/receive.png', confidence=0.6)
            if (_receive) and (_receive[0] > 0) and (_receive[1] > 0):
                dragto(_receive[0], _receive[1], 'left')
            else:
                moveto(w / 2, h / 2, 0.1)
                sleep(1)
                presskey('escape')
                sleep(1)
            # restart
            _start = pyautogui.locateOnScreen('C:/6000.png', confidence=0.6)
            if (_start) and (_start[0] > 0) and (_start[1] > 0):
                dragto(_start[0] + 382, _start[1] + 36, 'left')
            else:
                dragto(_getitems[0], _getitems[1], 'left')
        sleep(1)
        dragto(1585, 685, 'left')
        sleep(1)
        presskey('escape')
        sleep(1)
        moveto(w / 2, h / 2, 0.1)

def collect_booze():
    if (kill == True):
        return
    else:
        # nurition unit
        dragto(1115, 135, 'left')
        sleep(1)
        _button = pyautogui.locateOnScreen('C:/getitems.png', confidence=0.6)
        if (_button) and (_button[0] > 0) and (_button[1] > 0):
            sleep(1)
            # grab
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            # requirements
            presskey('y')
            sleep(1)
            # restart
            dragto(_button[0], _button[1], 'left')
            sleep(1)

        _button = pyautogui.locateOnScreen('C:/start.png', confidence=0.6)
        if (_button) and (_button[0] > 0) and (_button[1] > 0):
            sleep(1)
            # grab
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            dragto(_button[0], _button[1], 'left')
            sleep(1)
            # requirements
            presskey('y')
            sleep(1)
            # restart
            dragto(_button[0], _button[1], 'left')
            sleep(1)
        presskey('escape')
        sleep(1)

def collect_nutrition():
    if (kill == True):
        return
    else:
        # nurition unit
        dragto(1423, 192, 'left')
        sleep(1)
        # click scrollbar
        dragto(1888, 195, 'left')
        # scroll down
        for x in range(0, 10):
            presskey('down')
            sleep(1)
            _button = pyautogui.locateOnScreen('C:/getitems.png', confidence=0.6)
            if (_button) and (_button[0] > 0) and (_button[1] > 0):
                # grab
                sleep(1)
                dragto(_button[0], _button[1], 'left')
                sleep(1)
                dragto(_button[0], _button[1], 'left')
                sleep(1)
                # requirements
                presskey('y')
                sleep(2)
                # restart
                dragto(_button[0], _button[1], 'left')
                sleep(1)
                break
        presskey('escape')
        sleep(1)

def collect_hideout():
    global kill
    if (kill == True):
        return
    else:
        sleep(3)
        dragto(966, 868, 'left')
        sleep(3)
        presskey('enter')
        sleep(3)
        presskey('escape')
        sleep(3)
        dragto(1007, 291, 'left')
        sleep(1)
        moveto(w / 2, h / 2, 0.1)
        sleep(1)

        msg('Collecting Bitcoin.')
        collect_bitcoin()
        msg('Collecting Workbench.')
        collect_workbench()
        msg('Collecting Water.')
        collect_water()
        sleep(1)

        # recenter
        dragto(770, 283, 'left')
        sleep(1)
        presskey('escape')
        sleep(1)
        moveto(w / 2, h / 2, 0.1)

        #msg('Collecting Booze.')
        #collect_booze()
        #dragto(1027, 685, 'left')
        #sleep(1)

        msg('Collecting Nutrition.')
        collect_nutrition()
        dragto(504, 279, 'left')

        # recenter
        sleep(1)
        presskey('escape')
        sleep(1)
        moveto(w / 2, h / 2, 0.1)

        msg('Collecting Scavcase.')
        dragto(1400, 920, 'left')
        sleep(1)
        collect_scavcase()
        sleep(1)

        # recenter
        dragto(929, 341, 'left')
        sleep(1)
        presskey('escape')
        sleep(1)
        moveto(w / 2, h / 2, 0.1)

        # collect traders
        _traders = pyautogui.locateOnScreen('C:/traders.png', confidence=0.70)
        if (_traders) and (_traders[0] > 0) and (_traders[1] > 0):
            dragto(_traders[0] + 8, _traders[1] + 8, 'left')
        else:
            dragto(1110, 1065, 'left')
        msg('Navigating to traders menu.')
        collect_traders()

def collect_prapor():
    if (kill == True):
        return
    else:
        # select prapor
        select_trader('prapor')

        # select 545x39 BS
        dragto(260, 352, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('545x39 BS is out of stock.')

        # select 762x51r 7n1
        dragto(325, 356, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('762x51r 7n1 is out of stock.')

        # select 9x39 7n9 SPP
        dragto(76, 730, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('9x39 7n9 SPP is out of stock.')

        # select 762x51r 7n37
        dragto(195, 731, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('762x51r 7n37 is out of stock.')

        # select 762x51r 7BT1
        dragto(263, 729, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('762x51r 7BT1 is out of stock.')

        sleep(1)
        presskey('escape')
        sleep(1)

def collect_therapist():
    if (kill == True):
        return
    else:
        # select therapist
        select_trader('therapist')

        #select alu splint
        dragto(68, 353, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('Alu Splint is out of stock.')

        # select grizzly kit
        dragto(167, 432, 'left')
        sleep(2)
        if in_stock():
            dragto(945, 366, 'left')
            sleep(2)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('Grizzly Kit is out of stock.')

        sleep(1)
        presskey('escape')
        sleep(1)

def collect_skier():
    if (kill == True):
        return
    else:
        # select skier
        dragto(1234, 433, 'left')
        sleep(3)
        # select M855A1
        dragto(73, 294, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('M855A1 is out of stock.')

        # select 9mm Luger
        dragto(201, 297, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('9mm Luger is out of stock.')

        sleep(1)
        presskey('escape')
        sleep(1)

def collect_peacekeeper():
    if (kill == True):
        return
    else:
        # select peacekeeper
        select_trader('peacekeeper')

        # select M80
        dragto(334, 295, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('M80 is out of stock.')

        # select M856A1
        dragto(254, 346, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('M856A1 is out of stock.')

        # select 9MM 6.3 AP
        dragto(388, 354, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('9MM 6.3 AP is out of stock.')

        # select SS190
        dragto(81, 411, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('SS190 is out of stock.')

        # select M855A1
        dragto(145, 363, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('M855A1 is out of stock.')

        # select SB193
        dragto(455, 355, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in dollars
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('SB193 is out of stock.')

        sleep(1)
        presskey('escape')
        sleep(1)

def collect_mechanic():
    if (kill == True):
        return
    else:
        # select mechanic
        select_trader('mechanic')

        # select AP SX
        dragto(139, 288, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('AP SX is out of stock.')

        # select Sub SX
        dragto(205, 288, 'left')
        sleep(2)
        if in_stock():
            dragto(906, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('Sub SX is out of stock.')

        sleep(1)
        presskey('escape')
        sleep(1)

def collect_ragman():
    if (kill == True):
        return
    else:
        # select ragman
        select_trader('ragman')

        # select 6b43 goggles
        dragto(107, 728, 'left')
        sleep(2)
        if in_stock():
            dragto(945, 340, 'left')
            sleep(2)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(0.25)
            presskey('9')
            sleep(1)
            # fill in roubles
            dragto(837, 987, 'left')
            sleep(0.25)
            # click deal
            dragto(844, 170, 'left')
            sleep(1)
        else:
            msg('6b43 Goggles are out of stock.')

        sleep(1)
        presskey('escape')
        sleep(1)

def collect_misc():
    sleep(5)
    _y = 0
    dragto(947, 31, 'left')
    sleep(2)
    dragto(237, 88, 'left')

    for (idx, val) in enumerate(tobuy):
        sleep(1)
        if (kill == True):
            return
        else:
            dragto(237, 165 + _y, 'left')
            sleep(1)

            _button = pyautogui.locateOnScreen('C:/outofstock.png', confidence=0.6)
            _button2 = pyautogui.locateOnScreen('C:/locked.png', confidence=0.6)
            if (not _button) and (not _button2):
                dragto(1749, 185, 'left')
                sleep(2)
                dragto(1146, 482, 'left')
                sleep(1)
                if val == '12':
                    presskey('1')
                    sleep(1)
                    presskey('2')
                    sleep(1)
                else:
                    presskey(val)
                    sleep(1)
                sleep(1)
                presskey('y')
                sleep(2)
                dragto(953, 576, 'left')
        _y = _y + 34
    sleep(1)
    presskey('escape')
    sleep(1)

def collect_traders():
    global kill
    if (kill == True):
        return
    else:
        sleep(5)
        moveto(w / 2, h / 2, 0.1)
        sleep(1)
        msg('Collecting Prapor.')
        collect_prapor()
        #msg('Collecting Therapist.')
        #collect_therapist()
        msg('Collecting Skier.')
        collect_skier()
        msg('Collecting Peacekeeper.')
        collect_peacekeeper()
        msg('Collecting Mechanic.')
        collect_mechanic()
        #msg('Collecting Ragman.')
        #collect_ragman()
        #msg('Navigating wishlist.')
        #collect_misc()
        _market = pyautogui.locateOnScreen('C:/fleamarket.png', confidence=0.70)
        if (_market) and (_market[0] > 0) and (_market[1] > 0):
            dragto(_market[0] + 8, _market[1] + 8, 'left')
        else:
            dragto(1240, 1065, 'left')
        msg('Navigating to Flea Market.')
        flea_market()

def sell_bitcoins():
    if (kill == True):
        return
    else:
        sleep(5)
        moveto(w / 2, h / 2, 0.1)
        _traders = pyautogui.locateOnScreen('C:/traders.png', confidence=0.70)
        if (_traders) and (_traders[0] > 0) and (_traders[1] > 0):
            dragto(_traders[0] + 8, _traders[1] + 8, 'left')
        else:
            dragto(1110, 1065, 'left')
        moveto(800, h / 2, 0.1)

def flea_market():
    if (kill == True):
        return
    else:
        global autoselect
        sleep(5)
        moveto(w / 2, h / 2, 0.1)

        #if not autoselect:
        dragto(1237, 80, 'left')
        sleep(1)
        dragto(889, 187, 'left')
        sleep(1)
        #    autoselect = True
        #else:
        #    msg('Autoselect similar disabled.')

        for image, price in goods.items():
            dragto(1499, 88, 'left')
            sleep(1)
            dragto(1237, 80, 'left')
            sleep(1)
            moveto(883, 154, 0.2)
            sleep(1)
            dragto(883, 80, 'left', 2)
            sleep(1)
            dragto(1237, 80, 'left')
            sell_goods(image, price)
            sleep(1)

        moveto(w / 2, h / 2, 0.1)
        msg('Navigating back to hideout.')
        presskey('escape')

        _button = pyautogui.locateOnScreen('C:/bitcoin-marker.png', confidence=0.6)
        if (_button) and (_button[0] > 0) and (_button[1] > 0):
            # grab
            sleep(1)
            dragto(_button[0] - 32, _button[1], 'left')
            sleep(1)
            moveto(w / 2, h / 2, 0.1)
            sleep(1)
            presskey('escape')
            sleep(1)

        moveto(w / 2, h / 2, 0.1)
        for x in range(0, 3):
            sleep(1)
            presskey('escape')

        dragto(962, 868, 'left')
        moveto(w / 2, h / 2, 0.1)
        msg('All tasks completed closing.')
        sleep(1)
msg('Name: EFT Hideout, Trader, & Flea Market Automation\nAuthor: Clark\nWebsite: www.HavocGamers.net\n\nTo stop script press Control + Shift + F1.\n')
#flea_market()
#collect_traders()
collect_hideout()
