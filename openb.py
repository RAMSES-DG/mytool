
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


def openingb():
  print(" ")
  inp = (input(colors.WHITE+" mytool"+colors.RED+"( books : open ) > "+colors.WHITE))
  if inp == ("help"):
   print(" ")
   slprint (colors.ORANGE+openingb_help)
   openingb()
  if inp == ("help"):
   print(" ")
   slprint (colors.ORANGE+openingb_help)
  elif inp == ("back"):
   os.system (" python books.py ")
   sys.exit(0)
  elif inp == ("clear"):
   os.system ("clear")
   openingb()
  elif inp == ("show"):
   print(" ")
   slprint(colors.ORANGE+books+colors.WHITE)
   openingb()
  elif inp == ("cinfo"):
   slprint (colors.ORANGE+codes_info+colors.WHITE)
   openingb()
  elif inp == ("exit"):
   def exitopb():
     exitynopb = (input(colors.BLUE+"""
 do you want to exit ? ( y , n ) """))
     if exitynopb == ("y"):
      print(exthanks)
      sys.exit(0)
     elif exitynopb == ("n"):
      openingb()
     else:
      print(colors.RED+"""
 invailed command
                    ( you must type "y" or "n" )"""+colors.WHITE)
      exitopb()
   exitopb()
                                # books codes

  elif inp == "g1":
   os.system ( " open modules/books-prt/g-2/bokhary.pdf " )
   openingb()
  elif inp == "g2":
   os.system ( " open modules/books-prt/g-2/moslem.pdf " )
   openingb()
  elif inp == "f1":
   os.system ( " open modules/books-prt/f-3/1-2-3-4-5.pdf " )
   openingb()
  elif inp == "f2":
   os.system ( " open modules/books-prt/f-3/6-7-8-9-10.pdf " )
   openingb()
  elif inp == "f3":
   os.system ( " open modules/books-prt/f-3/11-12-13-14.pdf " )
   openingb()


                                # end

  else:
   print (colors.RED+"""
 [-] invailed command
                    ( press "help" to more infos ! )"""+colors.WHITE)

   openingb()
openingb()
