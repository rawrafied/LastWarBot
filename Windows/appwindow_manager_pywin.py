# -*- coding: utf-8 -*-
"""
INITIAL CREATION: Rawrafied 1/3/25
DESCRIPTION:
    - Class to manage interfacing with application
"""
# LIBRARY IMPORTS: ################################
import pywinauto
import pyautogui


import subprocess
import time

# ADBSERVER_MANAGER CLASS FUNCTIONS: ##########################
class appwindow_manager_pywin():
    # MAIN FUNCTION:
    def __init__(self, verbose):
        # INITIALIZE CLASS VARIABLES
        self.verbose = verbose
        self.appexedir = str('C:\\Users\\talks\\AppData\\Local\\TheLastWar\\Launch.exe')
        self.appopen = 0
        
        # INITIAL FUNCTION CALLS
        print("INITIALIZING APPWINDOW_MANAGER")
        self.open_window()
        self.gotovpscreen()
        
    # INITIALIZE CONNECTION BETWEEN SCRIPT AND APP
    def open_window(self):
        self.AppWindow = pywinauto.application().connection(title="Last War-Survival")
        print (self.AppWindow)
        
    
    # FUNCTION TO OPEN SECRETARY POSITION SCREEN: 
    def gotovpscreen(self):
        print("GOING TO VP DISPLAY")
        
            