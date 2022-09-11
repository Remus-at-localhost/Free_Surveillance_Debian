#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:13:06 2022

@author: Remus@localhost
"""

import json
import os
import requests
import time
import pyautogui as auto

main_dir = os.getcwd()        
stacks=[]
tokenid = []
with open(main_dir+'/Token_Url_Id.txt') as T:
    tokenid = T.readlines()
    Access_Token = tokenid[1][:-1]
    GID = tokenid[5][:-1]

headers = {"Authorization": Access_Token}

def retrieve():
    rec=requests.get(
        GID,headers=headers
    )
    jobj = json.loads(rec.text)
    for msg in jobj:
        #print(msg['content'])
        if msg['content']=="START":
            click()
            SysMsg('Connection with surveillance camera established..')
            SysMsg('Now use SHOW | CONT | STOP commands to control the system.')
            retrieve()

        elif msg['content']=="SHOW":
            uploader()
            retrieve()

        elif msg['content']=="CONT":
            uploader()                                        #This will post the image
            SysMsg('CONT')
            time.sleep(5)                                     #This will post the CONT commaand!
            retrieve()

        elif msg['content']=="STOP":
            SysMsg('System Offline!')
            exit()

        elif msg['content']=="SHUTDOWN":
            SysMsg('Shutting down..')
            SHUTDOWN()        

        else:
            retrieve()    

def SysMsg(message):

    payload = {
        "content":message
    }
    r = requests.post(
        GID,headers=headers,data=payload
    )


def click():
    time.sleep(4)
    auto.moveTo(350, 350)
    time.sleep(2)
    auto.click()
    time.sleep(2)
    auto.press('enter')
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

def uploader():
    for file in os.listdir():        #Included the Captures Folder here
        if file.__contains__(".jpeg"):                    #Jpeg files
 
            files = {
                #'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': open("./"+file, "rb")
            }
            r = requests.post(
                GID,
                headers=headers,
                files=files
            )
            print('SENT!')
            #os.remove(file)
            #time.sleep(2)
            #retrieve()
             #if flag == "single":
             #   retrieve()
            #else:
                #uploader('continious')
                #time.sleep(5)
                #retrieve()   ''' 
        else:
            pass

def SHUTDOWN():
    auto.moveTo(350,350)
    time.sleep(2)
    auto.click()
    time.sleep(2)
    auto.hotkey('alt','f4')
    time.sleep(2)
    auto.click()
    time.sleep(2)
    auto.hotkey('alt','f4')
    time.sleep(2)
    auto.moveTo(950,350)
    time.sleep(2)
    auto.click()
    time.sleep(2)
    exit()

SysMsg("Surveillance System Started on Linux Machine..")
SysMsg("Please wait for 30 seconds and then send START..")
retrieve()
