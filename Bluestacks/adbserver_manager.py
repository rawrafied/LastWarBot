# -*- coding: utf-8 -*-
"""
INITIAL CREATION: Rawrafied 1/3/25
DESCRIPTION:
    - Main script to instantiate Last War Bot environment.
"""
# LIBRARY IMPORTS: ################################
#import sys
#import os
import subprocess
#path = os.getcwd() # Check current directory's path

import time

from ppadb.client import Client as AdbClient

# ADBSERVER_MANAGER CLASS FUNCTIONS: ##########################
class adbserver_manager():
    # MAIN FUNCTION:
    def __init__(self, verbose):
        # INITIALIZE CLASS VARIABLES
        self.verbose = verbose
        
        # INITIAL FUNCTION CALLS
        print("INITIALIZING ADBSERVER_MANAGER")
        self.run_server()
        
    # INITIALIZE ADBSERVER TO INTERFACE WITH BLUESTACKS
    def run_server(self):
        # Run the adb server
        adbexe_hc = "C:/Users/talks/AppData/Local/Android/Sdk/platform-tools/adb.exe"
        #os.startfile(adbexe_hc)
        self.adbserver = subprocess.run([adbexe_hc, "start-server"])
        
        # List all devices
        #apk_path = "example.apk"
        #"HD-Player.exe"
        
        # Default is local host "127.0.0.1" and 5037
        self.clients = AdbClient(host="127.0.0.1", port=5037)
        self.devices = self.clients.devices()
        
        if self.verbose:
            print ("client =\n" + str(self.clients))
            print ("devices =\n" + str(self.devices))
        
        # CHECK IF NO DEVICES ARE RUNNING
        if len(self.devices) == 0:
            print("NO DEVICES RUNNING")
            # OPEN VP BOT BLUESTACKS
            lastwarexe = "C:\Program Files\BlueStacks_nxt\HD-Player.exe"
            instancet2r = "Pie64"
            #instancet2r = "Pie64_1"
            lastwarapp = 'com.fun.lastwar.gp'
            # CALL THE ANDROID-APP/PACKAGE VIA THE ADB SHELL COMMAND
            subprocess.run([lastwarexe, "shell", "--instance", instancet2r, "--cmd", "launchApp", "--package", 'com.fun.lastwar.gp'])
            time.sleep(20) #PAUSE FOR 20 SECS
            # CALL THE AUTOCLICKER APP
            
            
            