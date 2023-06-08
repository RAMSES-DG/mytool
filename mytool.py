
# my tool  ( by ramses )

          # imported libs && files


import time
import sys
import os
import random
from data import *
from data.helps import *
from data.lists import *
from data.randoms import *


          # codes of colors

class colors:
    BLUE        = '\033[94m'
    GREEN       = '\033[32m'
    RED         = '\033[0;31m'
    DEFAULT     = '\033[0m'
    ORANGE      = '\033[33m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    BR_COLOUR   = '\033[1;37;40m'
    BLACK       = '\033[30m'
    YELLOW      = '\003[33m'
    CYAN        = '\003[36m'

                           # here the script will strat 
 # slow print code

def slprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.005)

                  # password

def password() :
    print(" ")
    inp = (input(" enter password  :  "))
    if inp in pwd :
     print(colors.GREEN+"""
 [+] success login ...

""")
     slprint (colors.RED+logo_a+colors.GREEN+logo_b+colors.WHITE)
     os.system(" python restart.py")
    else :
     print(colors.RED+"""

 [-] failed login
             ( you must go to "password.py" file in "mytool" folder )
"""+colors.WHITE)
     password()
password()
