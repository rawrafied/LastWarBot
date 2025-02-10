# -*- coding: utf-8 -*-
"""
INITIAL CREATION: Rawrafied 1/3/25
DESCRIPTION:
    - Main script to instantiate Last War Bot environment.
"""
# LIBRARY IMPORTS: ################################
#import sys
#import os
#import subprocess
#path = os.getcwd() # Check current directory's path


# BOT LIBRARY FILES
import appwindow_manager_win

# TESTING VARIABLES: ##############################
# Variables:
verbose = False

if verbose:
    print ("test")

# VPBOT CLASS FUNCTIONS: ##########################
# MAIN FUNCTION:
def main():
    print("INITIALIZING VPBOT INTELLIGENCE ASSISTANCE CODE")
    
    #Variables:
    role =["VPBOT"] # Options: VPBOT, FARMER, FIGHTER
    firstopened = True
    
    appwindow_mgr = appwindow_manager_win.appwindow_manager(verbose)
    

# MAIN SOFTWARE ###################################
if __name__ == '__main__':
    main()