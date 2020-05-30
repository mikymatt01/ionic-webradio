import os
import time

ShoutcastPath=	'F:\\"Program Files"\\Shoutcast\\'
WinampPath   =	'F:\\"Program Files"\\Winamp\\'
NgrokPath    =  'C:\\Users\\utente\\Desktop\\radioLeo\\ngrok\\'
CleverPath   =  'C:\\Users\\utente\\Desktop\\radioLeo\\'

os.system('start ' + ShoutcastPath + 'sc_serv')
os.system('start ' + WinampPath	   + 'Winamp')
time.sleep(1)
os.chdir(CleverPath)
os.system('clever loadplay playlist')
os.chdir(NgrokPath)
os.system('ngrok.exe http --subdomain=davinciradio 8000')