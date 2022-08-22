#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:13:06 2022

@author: Remus@localhost
"""

import os
import requests
import time
import pyautogui as auto

main_dir = os.getcwd()        

tokenid = []
with open(main_dir+'/Token_Url_Id.txt') as T:
    tokenid = T.readlines()
    Access_Token = tokenid[1][:-1]
    GID = tokenid[5][:-1]

def click():
    time.sleep(30)
    
    auto.moveTo(350, 350)
    time.sleep(2)
    auto.click()
    time.sleep(2)
    auto.write('load stdapi')
    time.sleep(2)
    auto.press('enter')
    time.sleep(2)
    
    auto.write('webcam_stream')
    time.sleep(2)
    auto.press('enter')
    

    time.sleep(15)
    auto.click()
    time.sleep(2)
    auto.hotkey('alt','f4')
    time.sleep(2)
    uploader()



def uploader():
    for file in os.listdir():        #Included the Captures Folder here
        if file.__contains__(".jpeg"):                    #Jpeg files

            headers = {"Authorization": Access_Token}
 
            files = {
                #'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': open("./"+file, "rb")
            }
            r = requests.post(
                GID,
                headers=headers,
                files=files
            )
            print(r.text)
            os.remove(file)
            time.sleep(5)
            uploader()
        else:
            pass

click()

