
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



def restart():
     print(" ")
     inp = (input(colors.WHITE+" mytool > "+colors.WHITE))
     if inp == ("set dlinks"):                                                              # darkweb links 1
      os.system (" python dlinks.py ")
      sys.exit(0)

     elif inp == ("set tools"):
      os.system (" python tools.py")
      sys.exit(0)
     elif inp == ("set books"):
      os.system (" python books.py")
      sys.exit(0)
     elif inp == ("options"):
      slprint(colors.ORANGE+main_options)
      restart()
     elif inp == ("clear"):
      os.system ("clear")
      restart()
     elif inp == ("help"):
      slprint(colors.ORANGE+main_help)
      restart()
     elif inp == ("exit"):
      def exitm():
        exitynm = (input(colors.BLUE+"""
 do you want to exit ? ( y , n ) """))
        if exitynm == ("y"):
         print(exthanks)
         sys.exit(0)
        elif exitynm == ("n"):
          restart()
        else:
         print(colors.RED+"""
 [-] invailed command
                    ( you must type "y" or "n" )"""+colors.WHITE)
         exitm()
      exitm()
     else:
      print(colors.RED+"""
 [-] invaild command
               ( press "help" to more infos )"""+colors.WHITE)
      restart()
restart()
