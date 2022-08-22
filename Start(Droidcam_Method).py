#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:25:31 2022

@author: Remus@localhost
"""
import pyautogui as auto
import os
import time
import requests
import cv2
import numpy as np

sec=2
main_dir = os.getcwd()        

Input = []
with open(main_dir+'/Token_Url_Id.txt') as T:
    Input = T.readlines()
    Access_Token = Input[1][:-1]
    GID = Input[5][:-1]
    url = Input[8][:-1]


def initialise():
    a = input('\nPlease make sure that your browser and other programs are closed..\n Press any key to continue..')
    if a:
        pass
    print('Please dont touch your mouse and Keyboard..')
    time.sleep(sec)
  					#For Desktop_Automation
    auto.press('win')
    time.sleep(sec)
    auto.write('brave')			#Pls Replace the browser name here accordingly
    time.sleep(sec)
    auto.press('enter')
    time.sleep(5)
    auto.write(url)
    time.sleep(sec)
    auto.press('enter')
    time.sleep(5)
    Cleaner()
    ScreenShot()
    #auto.hotkey('alt','prtscr')
    
def Cleaner():
	for file in os.listdir(os.getcwd()):
        	if file.__contains__(".png"):
        		os.remove(file)
        		print("Removed " + file)
 
	   

def ScreenShot():
    ss = auto.screenshot(region=(228,102,899,665)) #Screen Coordinates for capture
    ss = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGR) #Placing this Screenshot into Numpy-array 
    cv2.imwrite('img2.png', ss)			       #Saving the Screenshot	 	
    time.sleep(3)
    uploader()
    
    

def uploader():
    for file in os.listdir():        			
        if file.__contains__(".png"):                   

            headers = {"Authorization": Access_Token}
 
            files = {
                #'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': open("./"+file, "rb")
            }
            r = requests.post(
                GID,				#posts to this Group
                headers=headers,		#using this Access token(Header)
                files=files			#Image -> Discord group 
            )
            print(r.text)			#Upload Log
            os.remove(file)			#Deleting the screenshot
            time.sleep(5)
            ScreenShot()			
        else:
            pass

    
initialise()    
   
