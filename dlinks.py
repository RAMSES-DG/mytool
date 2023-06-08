
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
 # slow print code

def slprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.005)


def dlinks():
  print(" ")
  inp = (input(colors.WHITE+" mytool"+colors.RED+"( dlink ) > "+colors.WHITE))
  if inp == ("help"):
   print(" ")
   slprint(colors.ORANGE+dlinks_help)
   dlinks()
  elif inp == ("clear"):
   os.system ("clear")
   dlinks()
  elif inp == ("exit"):
   def exitdl():
    exityndl = (input(colors.BLUE+"""
 do you want to exit ? ( y , n ) """))
    if exityndl == ("y"):
     print(exthanks)
     sys.exit(0)
    elif exityndl == ("n"):
     dlinks()
    else:
     print(colors.RED+"""
 [-] invailed command
                    ( you must type "y" or "n" )"""+colors.WHITE)
     exitdl()
   exitdl()
  elif inp == ("back"):
   os.system(" python restart.py ")
   sys.exit(0)

  elif inp == ("show"):
   print(" ")
   os.system (" nano modules/darkweb/darknet-links ")
   dlinks()
  else:
   print (colors.RED+"""
 [-] invailed command
                     ( press "help" to more infos ! )"""+colors.WHITE)
   dlinks()
dlinks()
