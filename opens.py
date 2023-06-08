
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



def opening():
  print(" ")
  inp = (input(colors.WHITE+" mytool"+colors.RED+"( tools : open ) > "+colors.WHITE))
  if inp == ("help"):
   print(" ")
   slprint (colors.ORANGE+opening_help)
   opening()
  elif inp == ("clear"):
   os.system ("clear")
   opening()
  elif inp == ("show"):
   print(" ")
   slprint(colors.GREEN+tools_tools1+colors.RED+tools_tools2+colors.GREEN+tools_tools3+colors.WHITE)
   opening()
  elif inp == ("exit"):
   def exitop():
     exitynop = (input(colors.BLUE+"""
 do you want to exit ? ( y , n ) """))
     if exitynop == ("y"):
      print(exthanks)
      sys.exit(0)
     elif exitynop == ("n"):
      opening()
     else:
      print(colors.RED+"""
 invailed command
                    ( you must type "y" or "n" )"""+colors.WHITE)
      exitop()
   exitop()

  elif inp == ("back"):
   os.system (" python tools.py")
   print (" ")

  elif inp == ("a1"):
   os.system("clear")
   print (colors.GREEN+"""

open metasploit-framework ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" msfconsole ")
   sys.exit(0)
  elif inp == ("a2"):
   os.system("clear")
   print (colors.GREEN+"""

open network map ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" nmap --help ")
   sys.exit(0)
  elif inp == ("a3"):
   os.system("clear")
   print (colors.GREEN+"""

open physical calculator ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" python /root/p-c/pc.py ")
   sys.exit(0)
  elif inp == ("a4"):
   os.system("clear")
   print (colors.GREEN+"""

open admin panal finder ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" python /root/Admin-Panel-Finder/ADMIN.py ")
   sys.exit(0)

  elif inp == ("a5"):
   os.system("clear")
   print (colors.GREEN+"""

open airgeddon ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" bash /root/airgeddon/airgeddon.sh ")
   sys.exit(0)

  elif inp == ("b1"):
   os.system("clear")
   print (colors.GREEN+"""

open cam hacker ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" bash /root/CamHacker/ch.sh ")
   sys.exit(0)

  elif inp == ("b2"):
   print(" ")
   print (colors.RED+"""

can't open dvr CVE-2018  ...

"""+colors.WHITE)
   time.sleep(2)
   opening()



  elif inp == ("b3"):
   os.system("clear")
   print (colors.GREEN+"""

open kalitorify ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" kalitorify --help ")
   sys.exit(0)
  elif inp == ("b4"):
   os.system("clear")
   print (colors.GREEN+"""

open onion share ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" flatpak run org.onionshare.OnionShare  ")
   sys.exit(0)
  elif inp == ("b5"):
   os.system("clear")
   print (colors.GREEN+"""

open phonesploit ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" python /root/PhoneSploit/phonesploit.py ")
   sys.exit(0)

  elif inp == ("c1"):
   os.system("clear")
   print (colors.GREEN+"""

open pyphisher ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" python /root/PyPhisher/pyphisher.py ")
   sys.exit(0)

  elif inp == ("c2"):
   os.system("clear")
   print (colors.GREEN+"""

open red hawk ...
"""+colors.WHITE)
   time.sleep(2)
   os.system (" php /root/RED_HAWK/rhawk.php ")
   sys.exit(0)

  elif inp == ("c3"):
   os.system("clear")
   print (colors.GREEN+"""

open routersploit ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" python /root/routersploit/rsf.py  ")
   sys.exit
  elif inp == ("c4"):
   os.system("clear")
   print (colors.GREEN+"""

open SARA ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" python /root/SARA/sara.py ")
   sys.exit(0)
  elif inp == ("c5"):
   os.system("clear")
   print (colors.GREEN+"""

open track ip ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" bash /root/track-ip/trackip ")
   sys.exit(0)
  elif inp == ("d1"):
   os.system("clear")
   print (colors.GREEN+"""

open wishfish ...

"""+colors.WHITE)
   time.sleep(2)
   os.system (" bash /root/WishFish/wishfish.sh ")
   sys.exit(0)



  else:
   print (colors.RED+"""
invailed command
                ( you must type correct code ! )"""+colors.WHITE)
   opening()
opening()
