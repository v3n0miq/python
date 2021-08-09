# -*- coding: utf-8 -*
#To download the new tools, you can enter this site
#https://1337w0rm.com/ 
#https://t.me/v3n0mhack
#####################################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
\033[36m Extract all sites on the server
   
\033[36m Blog :    https://1337w0rm.com
\033[36m Telgram : https://t.me/v3n0mhack
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
    
try:
    ooo = list((ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count

def revsip(url):
	try:
		grab = requests.get('https://sonar.omnisint.io/reverse/'+url, timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'})
		if 'null' in grab.text:
			print(kuning+'[+]' + url + abang + '>' +'Failed')
		else:
			result = json.loads(grab.text)
			print(kuning+'[+]' + birtu+'IP :'+' ' +ijo + str(url) +' '+'Total Domain =>' ), len(result)
			for domain in result: 
				ASU = domain.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
				open('grabbed.txt', 'a').write('http://' + ASU + "\n")
	except:
			pass

def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pp = pp.map(revsip, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
