import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
colorama.init()

CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'
RESET = '\033[0m'
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """         
                /|  /|  ---------------------------
                ||__||  |                         |
               /   O O\__  Po Jare Koe            |
              /          \ Asal Koe Bahagia       |
             /      \     \                       |
            /   _    \     \ ----------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \C_c_c_c    		         
			Unlimited Mass Domain To IP
		               MataKucing  
	      Cubjrnet7 - Noniod7 - AlifAlexis - ReoneH4x0r
      Lumajang Team Security - Lumajang Hack Team - Cukimay Cyber Team
      			 PT. Karang Jaya Abadi
"""
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.04)
logo()


def getIP(mk1337site):
	
		mk1337site = i.strip()
		try:
			if 'http://' not in mk1337site:
				LTSIP1 = socket.gethostbyname(mk1337site)
				print ("Duar! : "+LTSIP1)
				open('IPres.txt', 'a').write(LTSIP1+'\n')
			elif 'http://' in mk1337site:
				url = mk1337site.replace('http://', '').replace('https://', '').replace('/', '')
				LTSIP2 = socket.gethostbyname(url)
				print ("Duar! : "+LTSIP2)
				open('IPres.txt', 'a').write(LTSIP2+'\n')
	
		except:
			pass
			
mk1337=raw_input('Oper sitelist ing kate di dadine IP! : ')
with open(mk1337) as f:
    for i in f:
        getIP(i)
