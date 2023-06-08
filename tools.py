
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

def tools():
                                                             # tools 2
  print(" ")
  inp = (input(colors.WHITE+" mytool"+colors.RED+"( tools ) > "+colors.WHITE))
  if inp == ("help"):
   print(" ")
   slprint(colors.ORANGE+tools_help)
   tools()
  elif inp == ("clear"):
   os.system ("clear")
   tools()
  elif inp== ("exit"):
   def exitt():
     exitynt = (input(colors.BLUE+"""
 do you want to exit ? ( y , n ) """))
     if exitynt == ("y"):
      print(exthanks)
      sys.exit(0)
     elif exitynt == ("n"):
      tools()
     else:
      print(colors.RED+"""
 [-] invailed command
                    ( you must type "y" or "n" )"""+colors.WHITE)
      exitt()
   exitt()

  elif inp == ("back"):
   print(" ")
   os.system (" python restart.py ")
   sys.exit(0)
  elif inp == ("open"):
   os.system (" python opens.py ")
   sys.exit(0)
  else:
   print (colors.RED+"""
 [-] invailed command
                ( press "help" to more infos ! )"""+colors.WHITE)
   tools()
tools()
