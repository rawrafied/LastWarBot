# -*- coding: utf-8 -*-
"""
INITIAL CREATION: Rawrafied 1/3/25
DESCRIPTION:
    - Class to manage interfacing with application
"""
# LIBRARY IMPORTS: ################################
import win32gui
import win32con
import win32api

import subprocess
import time
from datetime import datetime

#TODO: Move to its own library
import pytesseract
from PIL import Image

# ADBSERVER_MANAGER CLASS FUNCTIONS: ##########################
class appwindow_manager():
    # MAIN FUNCTION:
    def __init__(self, verbose):
        # INITIALIZE CLASS VARIABLES
        self.verbose = verbose
        self.appexedir = str('C:\\Users\\talks\\AppData\\Local\\TheLastWar\\Launch.exe')
        #self.appexedir = str('LastWar')
        self.appopen = 0
        
        # INITIAL FUNCTION CALLS
        print("INITIALIZING APPWINDOW_MANAGER")
        self.open_window()
        self.gotovpscreen()
        print("INITIALIZATION DONE; RUNNING VP\nNOTE: Code is in progress. Temporary solution to exit program is by opening task manager via 'ctrl + shift + esc'")
        while True:
            self.runvp()
            currentmin = datetime.now().strftime("%M")
            print("Current min = "+currentmin)
            if int(currentmin) % 15 == 0:
                subprocess.call("TASKKILL /F /IM LastWar.exe", shell=True)
                # Restart program every 5 mins
                time.sleep(2)
                currenttime = datetime.now().strftime("%H:%M")
                print("INITIALIZING APPWINDOW_MANAGER @ "+str(currenttime))
                self.open_window()
                self.gotovpscreen()
                print("INITIALIZATION DONE; RUNNING VP\nNOTE: Code is in progress. Temporary solution to exit program is by opening task manager via 'ctrl + alt + del'")
                
                
        
    # INITIALIZE CONNECTION BETWEEN SCRIPT AND APP
    def open_window(self):
        self.AppWindow = win32gui.FindWindow(None, "Last War-Survival Game")
        print (self.AppWindow)
        
        if self.AppWindow:
            win32gui.ShowWindow(self.AppWindow, win32con.SW_RESTORE)
            AppWindowChild = win32gui.GetWindow(self.AppWindow,win32con.GW_CHILD)
            print (AppWindowChild)
            self.appopen = 1
        else:
            print("APP NOT OPEN; OPENING...")
            subprocess.call(self.appexedir)
            #subprocess.call("LastWar.exe")
            WAITTIME = 20
            time.sleep(WAITTIME)
            if self.verbose:
                print("WAITED " + str(WAITTIME) + " SECS")
            self.opengamescenarios()
    
    # SEND CLICKS TO GAME WINDOW
    #TODO: CURRENTLY RELIES ON MOVING CURSOR; WANT IT TO SEND CLICKS IN BCKGND
    def sendclick(self, x, y):
        WAITTIME = 1
        time.sleep(WAITTIME)
        if self.verbose:
            print("WAITED " + str(WAITTIME) + " SECS")
        self.AppWindow = win32gui.FindWindow(None, "Last War-Survival Game")
        rect = win32gui.GetWindowRect(self.AppWindow)
        lparam = win32api.MAKELONG(100,680) 
        if self.verbose:
            print(lparam)
            print (rect)
        win32api.SetCursorPos((x,y))
        win32api.PostMessage(self.AppWindow, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
        win32api.PostMessage(self.AppWindow, win32con.WM_LBUTTONUP, None, lparam)
    
    # FUNCTION TO OPEN SECRETARY POSITION SCREEN: 
    def gotovpscreen(self):
        print("GOING TO VP DISPLAY")
        #self.sendclick(360, 80) # Click icon
        #self.sendclick(760, 480) # Server num
        self.sendclick(360, 80) # Click icon
        self.sendclick(760, 280) # Server num
    
    # FUNCTION TO RUN VIP CLICKS
    def runvp(self):
        for x in range(5):
            if x < 3:
                self.sendclick(650 - 100*(x-1), 470) # Click Position
            else:
                self.sendclick(650 - 100*(x-4), 320) # Click Position
            self.sendclick(780, 590) # Click List
            self.sendclick(720, 190) # Click Accept First Entry
            self.sendclick(650, 660) # Click exit
            self.sendclick(650, 660) # Click exit
    def runvp_farleft(self):
        for x in range(5):
            if x < 3:
                self.sendclick(290 - 100*(x-1), 450) # Click Position
            else:
                self.sendclick(290 - 100*(x-4), 300) # Click Position
            self.sendclick(420, 590) # Click List
            self.sendclick(380, 170) # Click Accept First Entry
            self.sendclick(290, 650) # Click exit
            self.sendclick(290, 650) # Click exit
        
    def opengamescenarios(self):
        currentday = int(datetime.today().weekday()) # Mon =0; Sun =6
        currenthour = int(datetime.now().strftime("%H"))
        print("Current Day = "+str(currentday)+"; Current hour = "+str(currenthour))
        if currentday == 5 or(currentday == 6 and currenthour < 21) or (currentday == 4 and currenthour >= 21):
            print("TODAY IS SUNDAY; ACCOUNT FOR LOOT DOMINO.")
            #TEMP SOLN: on friday/saturday, loot domino. can exit via click outside menu.
            self.sendclick(360, 80) # Click icon
        #if currentday == 6:
            #TEMP SOLN: Click for when there's capitol war
            #self.sendclick(650, 450) # Click x
            