#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:41:21 2022

@author: Remus@localhost
"""

import os
import pyautogui as auto
import time

def driver():
    print('Please dont touch your mouse/keyboard..')
    time.sleep(2)

    auto.hotkey('ctrl', 'shift', 'n')
    time.sleep(2)
    auto.hotkey('win','left')
    time.sleep(2)
    auto.hotkey('ctrl', 'shift', 'n')
    time.sleep(2)
    auto.hotkey('win','right')
    time.sleep(2)
    auto.moveTo(350, 350)
    time.sleep(2)
    auto.click() 
    time.sleep(2)
    #auto.write('End')
    auto.write('bash Exploit.sh')
    time.sleep(2)
    auto.press('enter')
    time.sleep(2)

    auto.moveTo(950, 350)
    auto.click()
    auto.write('python3 Main.py')
    time.sleep(2)
    auto.press('enter')
    time.sleep(2)
    print('Waiting for the next time out..')
    time.sleep(2)

def close():
    time.sleep(2)
    auto.moveTo(350, 350)
    time.sleep(2)
    auto.click()
    time.sleep(2)
    auto.hotkey('alt','f4')
    time.sleep(2)
    auto.moveTo(950, 350)
    time.sleep(2)
    auto.click()
    time.sleep(2)
    auto.hotkey('alt','f4')
    time.sleep(2)
    #os.system('python3 Cleaner.py')
    
def cleaner():
    for file in os.listdir(os.getcwd()):
        if file.__contains__(".png"):
            os.remove(file)
            print("Removed " + file)
        elif file.__contains__(".html"):
            os.remove(file)
            print("Removed " + file)
        elif file.__contains__(".jpeg"):
            os.remove(file)
            print("Removed " + file)    

        else:
            pass
    
i = 1
while i<10:
    driver()
    time.sleep(900)
    close()
    time.sleep(2)
    cleaner()
    time.sleep(2)
