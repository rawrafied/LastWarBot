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

#import pytessract

# BOT LIBRARY FILES
import adbserver_manager

# TESTING VARIABLES: ##############################
# Variables:
verbose = 1

if verbose:
    print ("test")

# VPBOT CLASS FUNCTIONS: ##########################
# MAIN FUNCTION:
def main():
    print("INITIALIZING VPBOT INTELLIGENCE ASSISTANCE CODE")
    adbmgr = adbserver_manager.adbserver_manager(verbose)
    

# MAIN SOFTWARE ###################################
if __name__ == '__main__':
    main()